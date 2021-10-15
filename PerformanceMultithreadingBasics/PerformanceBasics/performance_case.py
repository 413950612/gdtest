#! -*- coding: utf-8 -*-

#! /user/bin/env python

#! @Time     : 2019/12/30 20:37

#! @Author   : huangyaoqing

#！@Contact  ：413950612@qq.com

#! @File     : performance_case.py

#! @Software : PyCharm Community Edition

#！@Project  ：$ {PROJECT_NAME}




# 性能并发测试：Python的标准库提供了两个模块(thread和threading)
import threading
from time import sleep

def test():
    print "I am testing code！"

def thd():              # 建立执行线程的函数

    Threads = []        # 创建数组

    for i in range(10):         # 循环10次，建立10个线程
        t = threading.Thread(target=test)           # 创建线程t，并使用threading.Thread()方法调用上一个函数test的方法

        Threads.append(t)           # 把线程t组装到Threads中
        t.setDaemon(True)      # 将子线程设置守护线程：主线程(main)发现没有活着的非守护子线程，所以父线程死掉了。子线程(thd)发现父线程死了，子线程也自杀。线程全部回收，达到并发。

    for t in Threads:
        t.start()               # 对10个线程进行启动

    for t in Threads:
        t.join()                # 等待10个子线程结束：在子线程（thd）完成运行结束之前，父线程（main）将一直被阻塞。直到子线程运行结束，父线程才运行到终止。

if __name__ == "__main__":
    thd()
    print "I am main code！"