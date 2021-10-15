#! -*- coding: utf-8 -*-

#! /user/bin/env python

#! @Time     : 2020/3/25 20:32

#! @Author   : huangyaoqing

#！@Contact  ：413950612@qq.com

#! @File     : MultithreadingMethod1.py

#! @Software : PyCharm Community Edition

#！@Project  ：InterfaceAutomation






# 将函数传递进Thread对象：程序启动了3个线程，并且打印了每一个线程的线程名字，处理重复任务就可以使用。

import threading

def thread_fun(num):
    for n in range(0, int(num)):
        print " I come from %s, num: %s" %( threading.currentThread().getName(), n)

def main(thread_num):
    thread_list = list()
    # 先创建线程对象
    for i in range(0, thread_num):
        thread_name = "thread_%s" %i
        thread_list.append(threading.Thread(target = thread_fun, name = thread_name, args = (20,)))

    # 启动所有线程
    for thread in thread_list:
        thread.start()

    # 主线程中等待所有子线程退出
    for thread in thread_list:
        thread.join()

if __name__ == "__main__":
    main(3)
