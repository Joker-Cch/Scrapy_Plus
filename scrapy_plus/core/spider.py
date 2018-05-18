#coding:utf-8

from scrapy_plus.http.request import Request
from scrapy_plus.item import Item

class Spider(object):

    #start_url = "http://www.baidu.com/"
    start_urls = []

    def start_requests(self):
        # request_list = []
        # for start_url in self.start_urls:
        #     request_list.append(Request(start_url))
        # return request_list
        # 将start_request处理为生成器，在Engine哪里进行迭代取出每个请求
        for start_url in self.start_urls:
            yield Request(start_url)

    def parse(self, response):
        yield Item(response.xpath("//title/text()")[0])

        #yield Item(response.url)
        #return Request(url)
