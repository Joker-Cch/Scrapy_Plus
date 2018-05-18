#coding:utf-8

# 创建线程池，用法和多进程池相同
#from multiprocessing.dummy import Pool
#from gevent.pool import Pool

from scrapy_plus.conf.default_settings import *
from scrapy_plus.utils.log import logger



if ASYNC_TYPE == "coroutine":
    from scrapy_plus.async.coroutine import Pool
    logger.info(u"正在启用协程异步模式")

elif ASYNC_TYPE == "thread":
    from multiprocessing.dummy import Pool
    logger.info(u"正在启用多线程异步模式")

else:
    raise Exception(u"不支持该异步类型")



from scrapy_plus.http.request import Request
from scrapy_plus.http.response import Response

from .scheduler import Scheduler
from .downloader import Downloader
from scrapy_plus.item import Item


from datetime import datetime



import time

class Engine(object):

    def __init__(self):
        #self.spiders =  spiders
        self.spiders = self._auto_import_module_cls(SPIDERS, True)
        self.scheduler = Scheduler()
        self.downloader = Downloader()
        #self.pipeline = Pipeline()
        #self.pipelines = pipelines
        self.pipelines = self._auto_import_module_cls(PIPELINES)
        #self.spider_middlewares = SpiderMiddlewares()
        #self.downloader_middlewares = DownloaderMiddlewares()
        #self.spider_mids = spider_mids
        self.spider_mids = self._auto_import_module_cls(SPIDER_MIDDLEWARES)
        self.downloader_mids = self._auto_import_module_cls(DOWNLOADER_MIDDLEWARES)
        #self.downloader_mids = downloader_mids
        # 创建线程池/协程池对象
        self.pool = Pool()
        self.total_response = 0
        self.is_running = True


    def _auto_import_module_cls(self, paths=[], isspider=False):
        import importlib
        if isspider:
            result = {}  # 如果是爬虫，返回给__init__(self) 就是字典
        else:
            result = [] # 如果不是爬虫，返回给__init__(self) 是 列表


        for path in paths:
            module_name = path[:path.rfind(".")]
            ret = importlib.import_module(module_name)

            cls_name = path[path.rfind(".")+1:]

            cls = getattr(ret, cls_name) # 根据绝对路径，返回指定文件里的指定类名的类对象

            if isspider:
                result[cls.name] = cls()
            else:
                result.append(cls())

        return result


    def start(self):
        start = datetime.now()
        logger.info("start time: {}".format(start))
        self._start_engine()
        stop = datetime.now()
        logger.info("stop time: {}".format(stop))
        time = (stop - start).total_seconds()
        logger.info("useing time: {}".format(time))

    def _callback(self, _):
        if self.is_running == True:
            """递归调用自身，执行_execute_request_response_item"""
            self.pool.apply_async(self._execute_request_response_item, callback = self._callback)

    def _start_engine(self):
        if ROLE == "master" or ROLE is None:
            # 处理start_urls里的请求
            if ASYNC_TYPE == "coroutine":
                logger.info(u"协程正在执行...")
            else:
                logger.info(u"子线程正在执行...")

            self.pool.apply_async(self._start_requests)

            #self._start_requests()

        if ROLE == "slave" or ROLE is None:
            # 通过settings 控制并发量
            for i in range(ASYNC_MAX_COUNT):
                if ASYNC_TYPE == "coroutine":
                    logger.info(u"协程正在执行...")
                else:
                    logger.info(u"子线程正在执行...")

                self.pool.apply_async(self._execute_request_response_item, callback = self._callback)

        # 处理调度器的请求
        while True:
            # 避免CPU疯狂空转，浪费资源
            time.sleep(0.01)
            #self._execute_request_response_item()
            # 当请求计数器和响应计数器相等时，表示所有请求已经处理结束
            # 且至少有一个响应处理完毕，循环退出（避免程序刚执行就退出）
            if self.total_response == self.scheduler.total_request and self.total_response != 0:
                self.is_running = False
                break

        self.pool.close() # 不再向线程池添加任务了，协程默认执行pass
        self.pool.join()  # 让主线程等待所有子线程执行结束

        logger.info(u"主线程执行结束")

    def _start_requests(self):
        """处理start_urls里的请求"""
        for spider_name, spider in self.spiders.items():
            # 1. 先构建爬虫发送的第一个请求
            start_request_list = spider.start_requests()
            for start_request in start_request_list:
                # 给每个请求添加所属的爬虫名属性
                start_request.spider_name = spider_name
                for spider_middleware in self.spider_mids:
                    #### 1.1 请求经过爬虫中间件预处理
                    start_request = spider_middleware.process_request(start_request)

                #################   注意点：  ##################
                # 2. 将请求交给调度器存储,(要在start_request_list里面、在spider_mids外面)
                # 否则中间件禁用后，请求无法添加到调度器中
                self.scheduler.add_request(start_request)


    def _execute_request_response_item(self):
        # 3. 获取调度器中的请求对象
        request = self.scheduler.get_request()
        if request is None:
            return

        for downloader_middleware in self.downloader_mids:
            ##### 3.1 将请求经过下载中间件预处理
            request = downloader_middleware.process_request(request)


        # 4. 将请求交给下载器下载，获取响应对象
        response = self.downloader.get_response(request)

        for downloader_middleware in self.downloader_mids:
            ##### 4.1 将响应经过下载中间件预处理
            response = downloader_middleware.process_response(response)


        # 5. 将响应对象交给spider解析
        #result = self.spider.parse(response)
        #results = self.spider.parse(response)
        # 动态获取对象的指定属性值（数字、字符串、方法）
        spider = self.spiders[request.spider_name]
        parse_func = getattr(spider, request.parse)
        results = parse_func(response)
        for result in results:
            # 6. 判断解析结果的类型，分别做处理
            if isinstance(result, Request):
                result.spider_name = request.spider_name

                #for spider_middleware in self.spider_mids:
                    #### 6.1 如果是请求对象，交给爬虫中间件预处理，再添加到请求队列中
                #    result = spider_middleware.process_request(result)
                self.scheduler.add_request(result)

            elif isinstance(result, Item):
                #for spider_middleware in self.spider_mids:
                    #### 6.2 如果是Item数据，交给爬虫中间件预处理，再交给管道
                #    result = spider_middleware.process_item(result)
                #self.pipeline.process_item(result)
                for pipeline in self.pipelines:
                    result = pipeline.process_item(result, spider)
            else:
                raise Exception("ERROR ：不能处理parse方法返回的数据")

        self.total_response += 1








