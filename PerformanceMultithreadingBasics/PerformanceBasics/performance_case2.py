#! -*- coding: utf-8 -*-

#! /user/bin/env python

#! @Time     : 2019/12/30 22:08

#! @Author   : huangyaoqing

#！@Contact  ：413950612@qq.com

#! @File     : performance2.py

#! @Software : PyCharm Community Edition

#！@Project  ：$ {PROJECT_NAME}







import threading
from time import sleep
'''
def a():
    x = 0
    while True:
        x = x+1
        # %d打印整数，%s打印字符串，\n换行，%()输出
        # x是整数，loop是字符串
        print "%d%s\n"%(x," loop ")
        sleep(10)
'''
def b():
    for i in range(4):
        i = i + 1

        print "%d%s"%(i,"loop")
        sleep(5)

def thd():
    Threads = []

    for i in range(3):
        #t = threading.Thread(target=a)
        t = threading.Thread(target=b)
        t.setDaemon(True)
        Threads.append(t)
        t.start()
        print "%d%s"%(i+1," child thread start ")
        #t.join()

        for t in Threads:
            t.join()
if __name__ == "__main__":

     print "main thread start"
     thd()
     print "main thread want to end in fact "
