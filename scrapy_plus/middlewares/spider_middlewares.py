#coding:utf-8

class SpiderMiddlewares(object):
    def process_request(self, request):
        print("在爬虫中间件中处理Request完毕...")
        return request


    def process_item(self, item):
        print("在爬虫中间件中处理Item完毕...")
        return item
