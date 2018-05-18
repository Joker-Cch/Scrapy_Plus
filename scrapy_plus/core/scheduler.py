#coding:utf-8

# try:
#     from Queue import Queue
# except ImportError:
#     from queue import Queue

from scrapy_plus.conf.default_settings import *
import six

if ROLE is None:
    from six.moves.queue import Queue
    from scrapy_plus.set import NormalFilterSet as Set
elif ROLE in ["master", "slave"]:
    from scrapy_plus.queue import Queue
    from scrapy_plus.set import RedisFilterSet as Set
else:
    raise Exception(u"框架不支持该模式 {}".format(ROLE))

from scrapy_plus.utils.log import logger

class Scheduler(object):
    def __init__(self):
        self.queue = Queue() # 保存请求对象
        self._filter_set = Set() # 保存请求指纹（目前是url）
        self.total_request = 0

    def add_request(self, request):
        """
        对请求去重，并添加不重复的请求到队列中
        """
        if not request.filter:
            logger.info(u"添加请求（dont filter) 成功: [{}] <{}>".format(request.method, request.url))
            self.queue.put(request)
            self.total_request += 1
            return

        # 生成每个请求的指纹数据
        fp = self._gen_fingerprint(request)

        if not self._filter_request(fp, request):
            # 添加请求到请求队列，添加指纹数据到指纹集合里
            logger.info(u"添加请求成功: [{}] <{}>".format(request.method, request.url))
            self.queue.put(request)
            self.total_request += 1
            self._filter_set.add_fp(fp)


    def get_request(self):
        """
        返回队列的请求对象
        """
        try:
            return self.queue.get(False) # 避免阻塞
        except:
            return None



    def _filter_request(self, fp, request):
        """
        判断是否是重复请求，如果是重复的返回True，否则返回False
        """
        if self._filter_set.is_filter(fp):
            logger.info(u"发现重复请求 : [{}] <{}>".format(request.method, request.url))
            return True
        else:
            return False


    def _gen_fingerprint(self, request):

        from hashlib import sha1
        import w3lib.url

        url = request.url
        method = request.method
        params = request.params
        data = request.data

        # url查询字符串规整
        url = w3lib.url.canonicalize_url(url)
        # 请求方法字符串统一转为大写
        method = method.upper()

        # 处理params为字符串
        params = params if params is not None else {}
        params = str(sorted(params.items()))

        # 处理data为字符串
        data = data if data is not None else {}
        data = str(sorted(data.items()))

        # 构建一个sha1对象
        sha1 = sha1()

        # update() 必须接收一个非Unicode字符串(Python2 str / Python3 bytes)
        sha1.update(self.utf8_str(url))
        sha1.update(self.utf8_str(method))
        sha1.update(self.utf8_str(params))
        sha1.update(self.utf8_str(data))

        # 生成16进制数的sha1值
        fp = sha1.hexdigest()

        return fp

    def utf8_str(self, string):
        if six.PY2:
            if isinstance(string, str):
                # Python2 非Unicode str
                return string
            else:
                # Python2 Unicode unicode
                return string.encode("utf-8")
        else:
            if isinstance(string, bytes):
                # Python3 非Unicode bytes
                return string
            else:
                # Python3 Unicode str
                return string.encode("utf-8")














