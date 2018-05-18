#coding:utf-8


class SpiderMiddlewares1(object):
    def process_request(self, request):
        print(u"SpiderMiddlewares1 process_request {}".format(request.url))
        return request

    def process_item(self, item):
        print(u"SpiderMiddlewares1 process_item {}".format(item.data))
        return item


class SpiderMiddlewares2(object):
    def process_request(self, request):
        print(u"SpiderMiddlewares2 process_request {}".format(request.url))
        return request

    def process_item(self, item):
        print(u"SpiderMiddlewares2 process_item {}".format(item.data))
        return item

