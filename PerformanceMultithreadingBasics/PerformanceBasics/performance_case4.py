#! -*- coding: utf-8 -*-

#! /user/bin/env python

#! @Time     : 2019/12/31 20:18

#! @Author   : huangyaoqing

#！@Contact  ：413950612@qq.com

#! @File     : performance_case4.py

#! @Software : PyCharm Community Edition

#！@Project  ：$ {PROJECT_NAME}








import threading
count = 0           # 定义一个全局变量作为成功次数的统计

def test(response):
    global count        # 声明引用全局变量
    r = response.status_code
    if r==200:
        count = count + 1

def main():
    Threads = []
    for i in range(10):
        t = threading.Thread(target=test)
        t.setDaemon(True)
        Threads.append(t)

    for t in Threads:
        t.start()

    for t in Threads:
        t.join()
        f = open('/Users/test.txt', 'w')
        f.write(count)
        f.close()
