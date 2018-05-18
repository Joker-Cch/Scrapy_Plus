#coding:utf-8


class Request(object):
    """
    框架内置的请求类，可以创建请求对象，并初始化参数
    """

    def __init__(self, url, method="GET", headers=None, params=None, data=None, parse="parse", filter = True, meta=None):
        self.url = url  # 请求的url地址
        self.method = method # 请求方法，默认是GET
        self.headers = headers  # 请求报头
        self.params = params  # 查询字符串
        self.data = data   # 表单数据
        self.parse = parse
        self.filter = filter
        self.meta = meta
