#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random

ipList = [{"192.168.1.1": 2}, {"192.168.1.2": 4}, {"192.168.1.3": 1}]

#简单轮训   
class RoundRobin_Simple(object):
    __pos = 0
    def __init__(self):
        pass
    
    def getServer(self, *args):
        if self.__pos > len(args) - 1:
            self.__pos = 0

        ip = list(args[self.__pos])[0]
        self.__pos += 1
        
        return ip
        
r = RoundRobin_Simple()
print "***********************************************************************************"
print "简单轮训："
for i in range(6):
    print "第%d次轮训："%i, r.getServer(*ipList)


    

# 方案二：加权轮训
# 缺点：同一时刻连续的请求本被打到同一台机器，未分散
class RoundRobin_Weight(object):
    __maxPos = 0
    __pos = 0
    __list = []

    def __init__(self, *args):
        self.__list.extend(args)
        for dic in args:
            self.__maxPos += list(dic.values())[0]

    def getServer(self):
        # 判断self.__pos在坐标轴的区间
        ip = ""
        pos = self.__pos

        if pos >= self.__maxPos:
            self.__pos = 0
            pos = self.__pos
        for dic in self.__list:
            if pos < list(dic.values())[0]:
                ip = list(dic)[0]
                break
            else:
                pos -= list(dic.values())[0]
        self.__pos += 1
        return ip


r2 = RoundRobin_Weight(*ipList)
print "***********************************************************************************"
print "加权轮训："
for i in range(1,11):
    print "第%d次轮训：" % i, r2.getServer()


#方案三：平滑加权轮训算法
#优点：同一时刻的请求被分散打到各个机器上
class  RoundRobin_WeightingSmoothing(object):
    __totalWeight = 0
    __ipList = []
    __weight = []
    __currentWeight = []

    def __init__(self, *args):
        for dic in args:
            ip = list(dic)[0]
            weight = list(dic.values())[0]
            currentWeight = 0
            self.__totalWeight += weight
            self.__ipList.append(ip)
            self.__weight.append(weight)
            self.__currentWeight.append(currentWeight)
    def getServer(self):
        for idx in range(len(self.__weight)):
            self.__currentWeight[idx] += self.__weight[idx]
        
        max_currentWeight = max(self.__currentWeight)
        max_currentWeight_idx = self.__currentWeight.index(max_currentWeight)
        ip = self.__ipList[max_currentWeight_idx]
        
        self.__currentWeight[max_currentWeight_idx] -= self.__totalWeight
        
        return ip
        

r3 = RoundRobin_WeightingSmoothing(*ipList)
print "***********************************************************************************"
print "平滑加权轮训算法："
for i in range(1,15):
    print "第%d次轮训：" % i, r3.getServer()