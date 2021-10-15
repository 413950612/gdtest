#! -*- coding: utf-8 -*-

#! /user/bin/env python

#! @Time     : 2019/12/30 22:44

#! @Author   : huangyaoqing

#！@Contact  ：413950612@qq.com

#! @File     : performance 3.py

#! @Software : PyCharm Community Edition

#！@Project  ：$ {PROJECT_NAME}





# 性能响应时间：可以用datetime()函数
from datetime import datetime
import threading

def test():
    time1 = datetime.now()
    Threads = []
    for i in range(10):
        t = threading.Thread(target=test)
        t.setDaemon(True)
        Threads.append(t)

    for t in Threads:
        t.start()

    for t in Threads:
           t.join()

    print "main thread end"

    time2 = datetime.now()
    time = time2-time1
    f = open(r'D:\\PyCharmProject\\performancedemo\\date_time\\test.txt', 'w')
    f.write(time)
    f.close()
