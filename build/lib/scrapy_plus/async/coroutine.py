#coding:utf-8

from gevent.pool import Pool as BasePool
from gevent.monkey import patch_all
patch_all()
# 将Python底层的网络库改为异步的库 scoket，当遇到网络IO阻塞的时候，会自动切换协程执行。


#gevent.sleep(0.1)

class Pool(BasePool):
    """继承gevent的Pool"""
    def apply_async(self, func, args=None, kwds=None, callback=None):
        # 当程序调用apply_async方法时，默认返回父类的apply_async方法处理
        return BasePool().apply_async(func = func, args = args, kwds = kwds, callback = callback)

        # Python3 可以用super() 来表示父类
        #return super().apply_async(func = func, args = args, kwds = kwds, callback = callback)

    def close(self):
        # 当程序调用 close方法时，默认执行pass（避免和多线程代码冲突）
        pass
