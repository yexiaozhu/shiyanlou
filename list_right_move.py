#！ /usr/bin/env python 3.5.2
#coding = utf-8
#author = yexiaozhu
a,b=map(int,input().split())
c=input().split()
print(b%a)
if b%a==0:
    print(" ".join(c))
else:
    print(c[-b%a:])
    print(c[:a-b%a])
    print(" ".join((c[-b%a:]+c[:a-b%a])) if a>1 else c[0])