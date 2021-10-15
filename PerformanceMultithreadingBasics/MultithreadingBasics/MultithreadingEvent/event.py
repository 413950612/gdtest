#! -*- coding: utf-8 -*-

#! /user/bin/env python

#! @Time     : 2020/3/25 22:33

#! @Author   : huangyaoqing

#！@Contact  ：413950612@qq.com

#! @File     : event.py

#! @Software : PyCharm Community Edition

#！@Project  ：InterfaceAutomation




import threading
import time

class MyThread(threading.Thread):
    def __init__(self, signal):
        threading.Thread.__init__(self)
        self.singal = signal

    def run(self):
        print "I am %s,I will sleep ..."%self.name
        self.singal.wait()
        print "I am %s, I awake..." %self.name

if __name__ == "__main__":
    singal = threading.Event()
    for t in range(0, 3):
        thread = MyThread(singal)
        thread.start()

    print "main thread sleep 3 seconds... "
    time.sleep(3)

    singal.set()