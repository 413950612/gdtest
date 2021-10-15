#! -*- coding: utf-8 -*-

#! /user/bin/env python

#! @Time     : 2020/3/25 20:38

#! @Author   : huangyaoqing

#！@Contact  ：413950612@qq.com

#! @File     : name.py

#! @Software : PyCharm Community Edition

#！@Project  ：InterfaceAutomation






# 可以为每一个thread指定name，默认的是Thread-No形式的。
import threading

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.setName("new" + self.name)                 # 当然你可以指定每一个thread的name，这个通过setName方法

    def run(self):
        print "I am %s" % (self.name)

if __name__ == "__main__":
    for i in range(0, 5):
        my_thread = MyThread()
        my_thread.start()