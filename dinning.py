# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 15:06:53 2020

@author: kdban\
problem: Dinning table
"""
def fact(i):
    results=[1,1,2,6,24,120,720,5040,40320,362880,3628800,39916800,479001600,62270208800,87178291200,20922789888000,
             355687428096000,6402373705728000,121645100408832000,2432902008176640000]
    return results[i]

def ncr(n,r):
    if(n==r or r==0):
        return 1
    if(r==1):
        return n
    result=fact(n)//fact(r)
    
    result=result//fact(n-r)
    return result

T=int(input("Enter test cases:"))
for case in range(T):
    r,n=list(map(int,input("Table:").split()))
    initial=n//r
    extra=n%r
    type1=initial+1
    type2=initial
    combinations=1
    
    print("type1",type1)
    print("type2",type2)
    
    for i in range(0,extra):
        combinations=combinations*ncr(n,type1)
        print("Combinations",combinations)
        print(n,'C',type1,end="")
        n=n-type1
    for i in range(extra,r):
        combinations=combinations*ncr(n,type2)
        print("Combinations",combinations)
        print(n,'C',type2,end="")
        n=n-type2

    print(combinations)
