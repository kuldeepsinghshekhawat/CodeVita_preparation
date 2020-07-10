# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 16:11:54 2020

@author: kdban
"""

N= int(input("Number"))
nums=list(map(int, input("String:").split()))
#print(nums)

nums.sort()
shortlist=nums[-6:]#highest 6 numbers
shortlist
#formula=(a+4b+6c+4d+e)*(b+4c+6d+4e+f)
#highest 2 in c,d then b,e then a,f
c=shortlist[-1]#1 highest number
d=shortlist[-2]#2nd ,,
e=shortlist[-3]#3rd
b=shortlist[-4]
a=shortlist[0]
f=shortlist[1]

result=sum([a,4*b,6*c,4*d,e])

result=result*sum([b,4*c,6*d,4*e,f])
print(result)


