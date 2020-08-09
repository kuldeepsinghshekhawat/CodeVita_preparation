# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 14:32:08 2020

@author:Kuldeep Singh 
Topic: Death Battle
Based on the Fact
"""



import math

fact=[1,1,2,6,24,120,720,5040,40320,362880,3628800,39916800,479001600,6227020800,87]

def minus(n1,n2):
    numerator=n1[0]*n2[1]-n2[0]*n1[1]
    denominator=n1[1]*n2[1]
    
    ans_numerator=numerator//math.gcd(numerator,denominator)
    ans_denominator=denominator//math.gcd(numerator,denominator)
    return [ans_numerator,ans_denominator]

def add(n1,n2):
    numerator=n1[0]*n2[1]+n2[0]*n1[1]
    denominator=n1[1]*n2[1]
    ans_numerator=numerator//math.gcd(numerator,denominator)
    ans_denominator=denominator//math.gcd(numerator,denominator)
    return [ans_numerator,ans_denominator]

def mult(n1,n2):
    numerator=n1[0]*n2[0]
    denominator=n1[1]*n2[1]
    ans_numerator=numerator//math.gcd(numerator,denominator)
    ans_denominator=denominator//math.gcd(numerator,denominator)
    return [ans_numerator,ans_denominator]


def exp(n1,k):
    ans=[1,1]
    for i in range(k):
        ans=mult(ans,n1)
    return ans


def nCr(n,r):
    if n==r or r==0:
        #print('ncr',n,r,1,1)
        return [1,1]
    if r==1 or r==n-1:
        #print('ncr',n,r,n,1)
        return [n,1]
    numerator=fact[n]
    denominator=fact[r]*fact[n-r]
    ans_numerator=numerator//math.gcd(numerator,denominator)
    ans_denominator=denominator//math.gcd(numerator,denominator)
    return [ans_numerator,ans_denominator]


T=int(input("Test cases"))
for case in range(T):
    A,H,L1,L2,M,C=list(map(int,input("Data").split()))
    P1,P2=0,0
    if(A+C)*M<H:
        print('RIP')
        continue
    if A*M >=H:
        P,P2=1,1
        numerator=P1/(math.gcd(P1,P2))
        denominator=P2/(math.gcd(P1,P2))
        print(f'{numerator}/{denominator}')
        continue
    
    remaining=H-(A*M)
    required_lucky_attacks=math.ceil(remaining/C)
    curr_frac=[0,1]
    prob_lucky=[L1//math.gcd(L1,L2),L2//math.gcd(L1,L2)]
    prob_not_lucky=minus([1,1],prob_lucky)
    
    for i in range(required_lucky_attacks,M+1):
        curr_prob=mult(nCr(M,i),exp(prob_lucky,i))
        curr_not_prob=exp(prob_not_lucky,M-i)
        curr_prob=mult(curr_prob,curr_not_prob)
        curr_frac=add(curr_frac,curr_prob)
        #print(curr_frac)
        #print("----")
    print(f'{curr_frac[0]}/{curr_frac[1]}')
    
    
    
"""
OUTPUT:
    Test cases2
    Data10 33 7 10 3 2

98/125

    Data10 999 7 10 3 2
RIP
""" 
    



