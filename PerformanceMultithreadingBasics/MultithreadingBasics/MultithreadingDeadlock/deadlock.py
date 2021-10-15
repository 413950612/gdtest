#! -*- coding: utf-8 -*-

#! /user/bin/env python

#! @Time     : 2020/3/25 21:02

#! @Author   : huangyaoqing

#！@Contact  ：413950612@qq.com

#! @File     : deadlock.py

#! @Software : PyCharm Community Edition

#！@Project  ：InterfaceAutomation





import threading

counterA = 0
counterB = 0

mutexA = threading.Lock()
mutexB = threading.Lock()

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        self.fun1()
        self.fun2()

    def fun1(self):
        global mutexA, mutexB
        if mutexA.acquire():
            print "I am %s , get res: %s" %(self.name, "ResA")

            if mutexB.acquire():
                print "I am %s , get res: %s" %(self.name, "ResB")
                mutexB.release()

        mutexA.release()

    def fun2(self):
        global mutexA, mutexB
        if mutexB.acquire():
            print "I am %s , get res: %s" %(self.name, "ResB")

            if mutexA.acquire():
                print "I am %s , get res: %s" %(self.name, "ResA")
                mutexA.release()

        mutexB.release()

if __name__ == "__main__":
    for i in range(0, 100):
        my_thread = MyThread()
        my_thread.start()