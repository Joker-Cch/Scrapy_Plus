#coding:utf-8


from scrapy_plus.utils.log import logger

class Pipeline(object):

    def process_item(self, item, spider):
        logger.info(u"Item数据为: {}".format(item.data))
