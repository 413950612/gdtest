#! -*- coding: utf-8 -*-

#! /user/bin/env python

#! @Time     : 2020/3/25 20:48

#! @Author   : huangyaoqing

#！@Contact  ：413950612@qq.com

#! @File     : lockmutex.py

#! @Software : PyCharm Community Edition

#！@Project  ：InterfaceAutomation




import threading
import time

counter = 0
mutex = threading.Lock()

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global counter, mutex
        time.sleep(1)
        if mutex.acquire():
            counter += 1
            print "I am %s, set counter:%s" % (self.name, counter)
            mutex.release()

if __name__ == "__main__":
    for i in range(0, 100):
        my_thread = MyThread()
        my_thread.start()