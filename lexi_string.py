# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 12:30:48 2020

@author: kdban
"""
test=int(input("Test data:"))
for i in range(test):
    alpha=input("1st string:")
    str1=input("2nd string:")
    l=[]
    for i in str1:
        l.append(i)
        di={}
        c=0
    for i in alpha:
        di[c]=i
        c=c+1
        s1=' '
    for j in di.values():
        if j in l:
            s1=s1+j
    print(s1)
    test-=1