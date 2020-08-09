# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 15:23:13 2020

@author: Kuldeep Singh Shekhawat
Topic: Europian Iteration
Based on the Roman Numbers

"""
def roman(number):
    digits=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
    symbols=['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
    ans=''
    
    curr_base=len(digits)-1
    while number>0 and curr_base>=0:
        quotient=number//digits[curr_base]
        number=number%digits[curr_base]
        
        ans=ans+(quotient*symbols[curr_base])
        curr_base=curr_base-1

    return ans

def get_value(k):
    value=ord(k)-ord('0')
    if value > 9:
        value=10+ord(k)-ord('A')
    return value


def get_in_base_decimal_value(N,base):
    value=0
    N=str(N)
    for index in range(len(N)):
        power=len(N)-index-1
        value=value+(get_value(N[index])*(base**(power)))
    return value
        

inp=int(input("Test data"))

N=inp
while 1<=N and N<=3999:
    roman_N=roman(N)
    #print(N)
    #print(roman_N)
    max_digit='0'
    for digit in roman_N:
        if get_value(digit)>get_value(max_digit):
            max_digit=digit
    min_base=get_value(max_digit)+1
    #print(min_base)
    N=get_in_base_decimal_value(roman_N,min_base)


print(N)




"""
OUTPUT
Test data1
45338950"""


