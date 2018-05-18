#coding:utf-8

import requests
from scrapy_plus.http.response import Response
from scrapy_plus.utils.log import logger

class Downloader(object):

    def get_response(self, request):
        if request.method.upper() == "GET":
            res = requests.get(
                request.url,
                headers = request.headers,
                params = request.params
            )

        elif request.method.upper() == "POST":
            res = requests.post(
                request.url,
                headers = request.headers,
                params = request.params,
                data = request.data
            )
        else:
            raise Exception("ERROR : 不支持该请求方法")

        logger.info(u"[{}] <{}>".format(res.status_code, res.url))
        return Response(
            res.url,
            res.status_code,
            res.headers,
            res.content
        )
