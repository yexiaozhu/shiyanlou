#!/usr/bin/env python 2.7.12
#coding=utf-8
#author=yexiaozhu

import os, sys
import jieba, codecs, math
import jieba.posseg as pesg

names = {} #姓名字典
relationships = {} #关系字典
lineNames = [] #每段内人物关系

jieba.load_userdict('dict.txt') #加载字典
with codecs.open('busan.txt', 'r', 'utf-8') as f:
    for line in f.readlines():
        poss = pesg.cut(line) #分词并返回该词词性
        lineNames.append([]) #为新读入的一段添加任务名称列表
        for w in poss:
            if w.flag != 'nr' or len(w.word) < 2:
                continue #当分词长度小于2或该分词词性不为nr认为该词不为人名
            lineNames[-1].append(w.word)
            if names.get(w.word) is None:
                names[w.word] = 0
                relationships[w.word] = {}
            names[w.word] += 1 #人物出现次数+1
    # for name , times in names.items():
    #     print name, times
    for line in lineNames: #对于每一段
        for name1 in line:
            for name2 in line: #每段中的任意两个人
                if name1 == name2:
                    continue
                if relationships[name1].get(name2) is None:
                    relationships[name1][name2] = 1 #若两个人尚未同事出现新建项
                else:
                    relationships[name1][name2] = relationships[name1][name2] + 1 #两人共同出现次数加1

with codecs.open('busan_node.txt', 'w', 'gbk') as f:
    f.write('Id Label Weight\r\n')
    for name, times in names.items():
        f.write(name + " " + name + " " + str(times) + "\r\n")

with codecs.open("busan_edge.txt", "w", "gbk") as f:
    f.write("Source Target Weight\r\n")
    for name, edges in relationships.items():
        for v, w in edges.items():
            if w > 3:
                f.write(name + " " + v + " " + str(w) + "\r\n")