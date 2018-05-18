#coding:utf-8

DEFAULT_LOG_FILENAME = "baidu.log"

SPIDERS = [
    "spiders.baidu.BaiduSpider",
    #"spiders.douban.DoubanSpider",
]

PIPELINES = [
    "pipelines.BaiduPipeline",
    #"pipelines.DoubanPipeline",
]

SPIDER_MIDDLEWARES = [
    #"spider_middlewares.SpiderMiddlewares1",
    #"spider_middlewares.SpiderMiddlewares2",
]


DOWNLOADER_MIDDLEWARES = [
    #"downloader_middlewares.DownloaderMiddlewares1",
    #"downloader_middlewares.DownloaderMiddlewares2"
]

ASYNC_MAX_COUNT = 10
#ASYNC_TYPE = "thread"
ASYNC_TYPE = "coroutine"


# redis队列默认配置
REDIS_QUEUE_NAME = 'request_queue'
REDIS_QUEUE_HOST = 'localhost'
REDIS_QUEUE_PORT = 6379
REDIS_QUEUE_DB = 7


# redis指纹集合默认配置
REDIS_SET_NAME = 'fingerprint_set'
REDIS_SET_HOST = 'localhost'
REDIS_SET_PORT = 6379
REDIS_SET_DB = 7

# 非分布式模式
ROLE = None

# 使用了任何一个，都表示分布式模式
#ROLE = "master"
#ROLE = "slave"
