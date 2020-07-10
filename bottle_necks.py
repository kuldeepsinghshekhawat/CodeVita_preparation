# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 12:11:13 2020

@author: kdban
"""
T=int(input("Test cases:"))
for case in range(T):
    n=int(input("Value:"))
    arr=list(map(int,input("Data").split()))
    print(arr)
    freq={}
    max_freq=-1
    for num in arr:
        if num in freq:
            freq[num]=freq[num]+1
        else:
            freq[num]=1
        
        max_freq=max(max_freq,freq[num])
    print(max_freq)            
    
    
    
    
    
    
