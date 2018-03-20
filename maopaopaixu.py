#!/usr/bin/python
# -*- coding: UTF-8  -*-
# author: yexiaozhu


def bubble(list):
    list_len = len(list)
    while list_len > 0:
        for j in range(list_len - 1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
            print('j:', j)
            print('list=', list)
        list_len -= 1
    print('list=', list)
list = [1, 25, 15, 7, 10, 5]
#list = [1, 25]
list = [1, 25, 15, 7, 10, 5, 6]
bubble(list)