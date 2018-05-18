#coding:utf-8


class DownloaderMiddlewares1(object):
    def process_request(self, request):
        print(u"DownloaderMiddlewares1 process_request {}".format(request.url))
        return request

    def process_response(self, response):
        print(u"DownloaderMiddlewares1 process_response {}".format(response.url))
        return response


class DownloaderMiddlewares2(object):
    def process_request(self, request):
        print(u"DownloaderMiddlewares2 process_request {}".format(request.url))
        return request

    def process_response(self,  response):
        print(u"DownloaderMiddlewares2 process_response {}".format(response.url))
        return response

