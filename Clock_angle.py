# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 12:45:01 2020

@author: Kuldeep Singh Shekhawat
"""

rotation_peroid=int(input("Rotation peroid"))
longitude=float(input("Longitude"))
#IST=UTC+(24/360)*82.5=UTC+5.38hrs
time_diff=(rotation_peroid*longitude)/360
time_diff=time_diff*60
#print(time_diff)
hour=time_diff//60
hour=hour%12
mins=time_diff%60

minute_angle=mins*6
hour_anlge=(hour*30)+(mins*30)//60

diff=abs(hour_anlge-minute_angle)
if diff>180:
    diff=360-diff
print("{:.2f}".format(diff))


