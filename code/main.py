#coding:utf-8


from scrapy_plus.core.engine import Engine

import time

if __name__ == "__main__":
    while True:
        engine = Engine()
        engine.start()
        time.sleep(5)


    # baidu_spider = BaiduSpider()
    # douban_spider = DoubanSpider()


    # # engine = Engine(baidu_spider)
    # # engine.start()

    # # engine = Engine(douban_spider)
    # # engine.start()

    # # 保存了多个爬虫对象的字典
    # spiders = {baidu_spider.name : baidu_spider, douban_spider.name : douban_spider}
    # pipelines = [BaiduPipeline(), DoubanPipeline()]
    # spider_mids = [
    #     SpiderMiddlewares1(),
    #     SpiderMiddlewares2()
    # ]

    # downloader_mids = [
    #     DownloaderMiddlewares1(),
    #     DownloaderMiddlewares2(),
    # ]

    # engine = Engine(
    #     spiders,
    #     pipelines,
    #     spider_mids,
    #     downloader_mids
        # )
