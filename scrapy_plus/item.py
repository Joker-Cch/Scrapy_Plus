#coding:utf-8


class Item(object):
    """
    框架内置的item类，可以创建保存数据的item对象，提供了data方法用于访问数据
    """
    def __init__(self, data):
        self._data = data


    @property
    def data(self):
        return self._data
