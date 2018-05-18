#coding:utf-8

from scrapy_plus.core.spider import Spider
from scrapy_plus.http.request import Request
from scrapy_plus.item import Item

import time

class BaiduSpider(Spider):
    name = "baidu"

    start_urls = [
        "http://news.baidu.com/",
        "http://www.baidu.com/",
        "http://news.baidu.com/"
    ]

    def start_requests(self):
        for start_url in self.start_urls:
            yield Request(start_url, filter=False)

