#coding:utf-8

from scrapy_plus.core.spider import Spider
from scrapy_plus.http.request import Request
from scrapy_plus.item import Item


class DoubanSpider(Spider):
    name = "douban"
    #start_urls = ["https://movie.douban.com/top250?start=" + str(page) for page in range(0, 226, 25)]
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    def start_requests(self):
        start_urls = ["https://movie.douban.com/top250?start=" + str(page) for page in range(0, 226, 25)]


        for start_url in start_urls:
            yield Request(start_url, headers = self.headers)

    def parse(self, response):
        for node in response.xpath("//div[@class='hd']"):
            title = node.xpath(".//span[@class='title'][1]/text()")[0]
            yield Item(title)

            #link = node.xpath("./a/@href")[0]
            #yield Request(link ,headers = self.headers, parse = "parse_next")

    #def parse_next(self, response):
    #    yield Item(response.xpath("//title/text()")[0].strip())
