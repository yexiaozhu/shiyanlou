#!/usr/bin/python
# -*- coding: UTF-8  -*-
# author: yexiaozhu


def isHappy(n):
    if n is None:
        print('not')
        
    while n !=1 and n !=4:
        nums = list(str(n))
        n = 0
        for i in nums:
            n += int(i)**2
    print(n)
    if n == 1:
        print('yes')
    if n == 4:
        print('not')
        
n = input('请输入数字：')
isHappy(n)