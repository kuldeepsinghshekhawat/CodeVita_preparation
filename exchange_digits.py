# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 16:48:15 2020

@author: Kuldeep Singh Shekhawat
"""

from itertools import permutations
value,compare=input("Value").split()
compare=int(compare)

a=str(value)
a=''.join(sorted(a))
b=str(compare)
if len(a)<len(b):
    print(-1)
else:
    result=-1
    permlist=permutations(a)
    for i in list(permlist):
        str1=''.join(i)
        n=int(str1)
        if (n>compare):
            result=n
            break
    print(result)
    
    


