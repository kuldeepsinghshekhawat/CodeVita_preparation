# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 11:25:37 2020

@author: kdban
"""
def largest(num):
    num_str=str(num)
    i=9
    while i>= 0:
        if str(i) in num_str:
           return i
        i-= 1
      
def smallest(num):
    num_str=str(num)
    i=0
    while i<= 9:
        if str(i) in num_str:
            return i
        i+= 1
            


def pairs_from(num):
    if num==2:
        return 1
    if num>=3:
        return 2
    return 0



T=int(input("Test cases"))
for case in range(T):
    N=int(input("Data"))
    nums=list(map(int,input("Enter:").split()))
    assert(len(nums)==N)
    bitscore=[""]*N #string array

    for i in range(len(bitscore)):
        curr_score=str(11*largest(nums[i])+7*smallest(nums[i]))
        if len(curr_score) > 2:
            curr_score=curr_score[-2:]
        bitscore[i]=curr_score
    
    
    odd_pos_frq=[0]*10
    even_pos_frq=[0]*10

    for i in range(len(bitscore)):
        index=int(bitscore[i][0])
        if(i+1)%2==0:
            even_pos_frq[index]+= 1
        else:
            odd_pos_frq[index]+= 1
    
    count_pairs=[0]*10
    for i in range(10):
        if even_pos_frq[i] <= 1 and odd_pos_frq[i]<= 1:
            continue
        count_pairs[i]+= pairs_from(even_pos_frq[i])+pairs_from(odd_pos_frq[i])
        count_pairs[i]=min(2,count_pairs[i])
    print(sum(count_pairs))