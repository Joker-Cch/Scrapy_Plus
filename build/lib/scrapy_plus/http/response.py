#coding:utf-8


from lxml import etree
import json
import re

class Response(object):
    """
    框架内置的响应类，可以创建响应对象，并初始化参数
    """
    def __init__(self, url, status_code, headers, body):
        self.url = url # 响应的url
        self.status_code = status_code # 响应的状态码
        self.headers = headers # 响应报头
        self.body = body # 响应体内容

    def xpath(self, rule):
        html_obj = etree.HTML(self.body)
        return html_obj.xpath(rule)

    # 将网页返回的json字符串，转为Python数据类型
    @property
    def json(self):
        return json.loads(self.body)


    def re_findall(self, rule, string=None):
        if string is None:
            string = self.body
        return re.findall(rule, string)

