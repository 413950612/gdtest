#! -*- coding: utf-8 -*-

#! /user/bin/env python

#! @Time     : 2020/3/25 20:38

#! @Author   : huangyaoqing

#！@Contact  ：413950612@qq.com

#! @File     : join.py

#! @Software : PyCharm Community Edition

#！@Project  ：InterfaceAutomation








# 是用来阻塞当前上下文，直至该线程运行结束。
import threading

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.setName("new" + self.name)

    def join(self, timeout=10):         # timeout可以设置超时时间

        return timeout

    def run(self):
        print "I am %s" % (self.name)

if __name__ == "__main__":
    for i in range(0, 5):
        my_thread = MyThread()
        my_thread.start()