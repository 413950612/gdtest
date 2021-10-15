#! -*- coding: utf-8 -*-

#! /user/bin/env python

#! @Time     : 2020/3/25 20:32

#! @Author   : huangyaoqing

#！@Contact  ：413950612@qq.com

#! @File     : MultithreadingMethod2.py

#! @Software : PyCharm Community Edition

#！@Project  ：InterfaceAutomation







# 继承自threading.Thread类:
import threading

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print "I am %s" %self.name

if __name__ == "__main__":
    for thread in range(0, 5):
        t = MyThread()
        t.start()
