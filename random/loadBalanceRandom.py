#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random

#方案一：
class Random(object):
     # 直接随机： 缺点是每台机器性能不同，对任务处理能力也不同
    __ipList = []
    def __init__(self, *args):
        self.__ipList = args
    
    def getServer(self):
        idx = random.randint(0, len(self.__ipList)-1)
        return self.__ipList[idx]

ipList = [{"192.168.1.1": 1}, {"192.168.1.2": 5}, {"192.168.1.3": 1}]
r = Random(*ipList)
print "***********************************************************************************"
print "方案一随机ip: ", r.getServer()


#方案二：
class Random2(object):
    __ipList = []
    def __init__(self, *args):
        #根据权重往列表里添加多个ip, 例如{“192.168.1.2”：5},则添加5个该ip
        #缺点：如果权重值很大，则导致list内元素非常多，占内存
        for dic in args:
            for k,v in dic.items():
                while v > 0:
                    self.__ipList.append(k)
                    v = v - 1

    def getServer(self):
        idx = random.randint(0, len(self.__ipList) - 1)
        return self.__ipList[idx]

r2 = Random2(*ipList)
print "***********************************************************************************"
print "方案二随机ip: ", r2.getServer()

#方案三
class Random3(object):
    
    # 利用坐标轴随机一数字，查看该数字所在的区间范围
    def __init__(self):
        pass

    def getServer(self, *args):
        num = 0
        for dic in args:
            for ip, weight in dic.items():
                num += weight

        randomNum = random.randint(0, num - 1)

        for dic in args:
            for ip, weight in dic.items():
                if randomNum < weight:
                    return ip
                else:
                    randomNum = randomNum - weight



r3 = Random3()
print "***********************************************************************************"
print "方案三随机ip: "
for i in range(14):
    print "第%d次随机ip: "%i, r3.getServer(*ipList)