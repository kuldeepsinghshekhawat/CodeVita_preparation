# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 12:49:34 2020

@author: kdban
"""


def solution3():
    try:
        N = int(input("Data"))
    except:
        return 0 
        
    SZ = 1001
    grid = [[0] * SZ for i in range(SZ)]
    min_x = min_y = float("inf")
    max_x = max_y = float("-inf")
    for i in range(N):
        x1, y1, x2, y2, c = map(int, input("Enter").split())
        min_x = min(min_x, x1)
        min_y = min(min_y, y1)
        max_x = max(max_x, x2)
        max_y = max(max_y, y2)
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if grid[i][j] == 0:
                    grid[i][j] = c
                elif grid[i][j] > 0:
                    grid[i][j] = -(grid[i][j] + c)
                else:
                    grid[i][j] -= c
            
    cost = 0
    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):
            if grid[i][j] < 0:
                cost += grid[i][j]
 
    return -cost
 
print( solution3())