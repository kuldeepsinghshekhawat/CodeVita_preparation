# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 16:25:30 2020

@author:Kuldeep Singh Shekhawat
"""


value=int(input("Value"))
five=int((value-4)/5)
if (value-five*5)%2==0:
    one=2
else:
    one=1
    
two=int((value-5*five-1*one)/2)


print(five+two+one,five,two,one)




