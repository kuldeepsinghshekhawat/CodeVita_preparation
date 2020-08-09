# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 15:53:59 2020

@author: Kuldeep Singh Shekhawat
"""

number=int(input("Data"))
divisors=list()
for i in range(1,int(number**0.5)+1):
    if number%i==0:
        print(i,end=" ")
        if(number/i!=i):
            divisors.append(int(number/i))

divisors.sort()

print(*divisors,end=" ")

        



"""
Input:
    Data10
OUTPUT:
    
1 2 5 10
"""