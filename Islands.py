# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 13:52:12 2020

@author: kdban

Take input
Assume you have other vertices
Calculate manhattan distance to each vertex and store the min distance form warship
Finally sort the array based on distance, index


"""

def manhatten(x,y,a,b):
    man_distance=abs(x-a)+abs(y-a)
    return man_distance

def distance_from_warship(island,a,b):
    x1,y1=island["x1"],island["y1"]
    x2,y2=island["x2"],island["y2"]
    x3,y3=(x1+x2+y2-y1)/2,(y1+y2+x1-x2)/2
    x4,y4=(x1+x2+y1-y2)/2,(y1+y2+x2-x1)/2  
    
    distance=min(manhatten(x1,y1,a,b),manhatten(x2,y2,a,b), manhatten(x3,y3,a,b),  manhatten(x4,y4,a,b))
    
    return distance
    

N=int(input("Islands:"))
islands=[]
for index in range(N):
    x1,y1,x2,y2=list(map(int,input().split()))
    curr_island={
            "x1":x1,
            "y1":y1,
            "x2":x2,
            "y2":y2,
            "index":index+1
            }
    islands.append(curr_island)
a,b=list(map(int,input().split()))
    #sort the island
islands.sort(key=lambda x: distance_from_warship(x,a,b))
for island in islands:
    print(island["index"],end='')
    
    



"""
Islands:2

0 0 1 1 

0 3 1 4

0 0
12

"""
