#coding:utf-8

import redis


client = redis.Redis(db=7)

name = "fp_set"
result = client.sadd(name, "hello world!")
print(result)

result = client.sismember(name, "hello world!!!!")
print(result)


# list队列  FIFO模式

# lpush() ： 从左边插入一条数据
# 4 3 2 1

# lpop() : 从左边取出数据（取最后放入的） LIFO
# rpop() : 从右边取出数据（取最先放入的） FIFO



# rpush() : 从右边插入一条数据
# 1 2 3 4

# lpop() : 从左边取出数据（取最先放入的） FIFO
# rpop() : 从右边取出数据（取最后放入的） LIFO


# lpush() 存 + rpop() 取 == FIFO





# import pickle #
# import json

# # json.dumps() --> 将Python对象转为json字符串
# # json.loads() -> 将json字符串转为Python对象

# # pickle.dumps() -> 将Python对象 转为 二进制字符串数据
# # pickle.loads() -> 将二进制字符串数据 转为 Python对象



# from scrapy_plus.http.request import Request

# client = redis.Redis(db=7)

# name = "queue"
# data = Request("http://www.baidu.com/")

# r_data = pickle.dumps(data)
# client.lpush(name, r_data)

# result = client.rpop(name) # 字符串
# request = pickle.loads(result) # 将二进制字符串转回为对应的对象


# print(request)
# print(type(request))













