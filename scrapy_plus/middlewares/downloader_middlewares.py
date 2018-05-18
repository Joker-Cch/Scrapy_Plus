#coding:utf-8

class DownloaderMiddlewares(object):

    def process_request(self, request):
        print("在下载中间件中处理Request完毕...")
        return request


    def process_response(self, response):
        print("在下载中间件中处理Response完毕...")
        return response
