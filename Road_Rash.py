# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 14:01:27 2020

@author: kdban
"""

import  math
total_cars=int(input("Total Cars:"))
freq={}
total_collisions=0
for i in range(total_cars):
    curr_x,curr_y,curr_speed=list(map(int,input("DATA").split()))
    #time=distance/speed
    distance=math.sqrt(curr_x**2+curr_y**2)
    curr_time=distance/curr_speed
    if curr_time in freq:
        freq[curr_time]+=1
    else:
        freq[curr_time]=1
    total_collisions=total_collisions+freq[curr_time]-1   
print(total_collisions)
print(freq)




"""
output

Total Cars:5

DATA5 12 1

DATA16 63 5

DATA-10 24 2

DATA7 24 2

DATA-24 2 2 
3
{13.0: 3, 12.5: 1, 12.041594578792296: 1}
"""