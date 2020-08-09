# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 11:05:56 2020

@author: Kuldeep Singh Shekhawat
"""

import math
def mult(a,b,prime):
    ans=(a%prime * b%prime)%prime
    return ans

K=int(input("K"))
max_n=1000
prime=10**9+7

pascals=[[0 for i in range(max_n+1)] for j in range(max_n+1)]

pascals[0][0]=1
for i in range(1,len(pascals)):
    pascals[i][0]=1
    for j in range(1,i+1):
        pascals[i][j]=(pascals[i-1][j-1]+pascals[i-1][j])%prime
        
        
for case in range(K):
    N,T,M=list(map(int,input("Data").split()))\
    
    if N-M<T:
        print(1)
        continue
    if M==0:
        print(0)
        continue
    
    denominator=pascals[N][T]
    numerator=pascals[N-M][T]
    
    p=denominator-numerator
    q=denominator
    
    common=math.gcd(p,q)
    p=p//common
    q=q//common


    q_inv=pow(q,prime-2,prime)
    ans=mult(p,q_inv,prime)
    print(ans)
    

