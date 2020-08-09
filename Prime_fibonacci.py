# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 09:57:11 2020

@author: Kuldeep Singh Shekhawat
"""


def get_primes(start,end):
    prime_100=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
    start_idx=0
    end_idx=len(prime_100)-1
    
    while(start_idx <= end_idx and prime_100[start_idx]<start):
        start_idx+= 1
        
    while(end_idx >= start_idx and prime_100[end_idx]>end):
        end_idx-= 1
    
    req_list=prime_100[start_idx:end_idx+1]
    return req_list


def get_combinations(original_list):
    combinations_list=[]
    for i in range(len(original_list)):
        for j in range(len(original_list)):
            if i!=j:
                combined=str(original_list[i])+str(original_list[j])
                combined=int(combined)
                if isPrime(combined):
                    combinations_list.append(combined)
    combinations_list=list(set(combinations_list))
    return combinations_list

 
def isPrime(num):
    if num%2==0:
        return False
    if num <2:
        return False
    i=2
    while(i*i<=num):
        if num%i==0:
            return False
        i+= 1
    return True

def get_last_fibonacci(first,second,n):
    if n==1:
        return first
    if n==2:
        return second
    for i in range(3,n+1):
        ans=first+second
        first=second
        second=ans
        
T=int(input("Test case"))
for case in range(T):
    n1,n2=list(map(int,input("Data").split()))
    primes_list=get_primes(n1,n2)
    combinations_list=get_combinations(primes_list)
    smallest_a=min(combinations_list)
    largest_b=max(combinations_list)
    fib_no=len(combinations_list)
    ans=get_last_fibonacci(smallest_a,largest_b,fib_no)
    
    print(ans)

  

"""
Input Format
1
2 40

Output

13158006689
"""
