# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 13:00:36 2020

@author: Kuldeep Singh Shekhawat Chirana
Topic:Minimum queens queen's life

"""

def find_max(queen,grid,visited,adjacency):
    curr_x=queen[0]
    curr_y=queen[1]
    name=queen[2]
    ans=1
    visited.add(name)
    if len(adjacency[name])==0:
        visited.remove(name)
        return ans
    for q in adjacency[name]:
        if q[2] not in visited:
            path=find_max(q,grid,visited,adjacency)
            ans=max(1+path,ans)
    visited.remove(name)
    return ans


def from_neighbours(adjacency,q,grid):
    curr_x=q[0]
    curr_y=q[1]
    curr_name=q[2]
    for x in range(curr_x-1,-1,-1):
        if grid[x][curr_y]!='-':
            adjacency[curr_name].append((x,curr_y,grid[x][curr_y]))
            break
    for x in range(curr_x+1,len(grid)):
        if grid[x][curr_y]!='-':
            adjacency[curr_name].append((x,curr_y,grid[x][curr_y]))
            break

    for y in range(curr_y-1,-1,-1):
        if grid[curr_x][y]!='-':
            adjacency[curr_name].append((curr_x,y,grid[curr_x][y]))            
            break

    for y in range(curr_y+1,len(grid)):
        if grid[curr_x][y]!='-':
            adjacency[curr_name].append((curr_x,y,grid[curr_x][y]))
            break
    
    for i in range(1,len(grid)):
        if curr_x+i < len(grid) and curr_y+i<len(grid) and grid[curr_x+i][curr_y+i]!="-":
            adjacency[curr_name].append((curr_x,y,grid[curr_x+i][curr_y+i]))
            break
    for i in range(1,len(grid)):
        if curr_x+i < len(grid) and curr_y-i>=0 and grid[curr_x+i][curr_y-i]!="-":
            adjacency[curr_name].append((curr_x,y,grid[curr_x+i][curr_y-i]))
            break
            
            
    for i in range(1,len(grid)):
        if curr_x-i>=0 and curr_y+i<len(grid) and grid[curr_x-i][curr_y+i]!="-":
            adjacency[curr_name].append((curr_x,y,grid[curr_x-i][curr_y+i]))
            break
            
            
    for i in range(1,len(grid)):
        if curr_x-i >=0 and curr_y-i >=0 and grid[curr_x-i][curr_y-i]!="-":
            adjacency[curr_name].append((curr_x,y,grid[curr_x-i][curr_y-i]))
            break
        
N,M=list(map(int,input("Data").split()))
grid=[['-' for i in range(N)] for x in range(N)]
queens=[]

for _ in range(M):
    x,y,q=input("Pass Data").split(',')
    x=int(x)
    y=int(y)
    grid[x-1][y-1]=q
    queens.append((x-1,y-1,q))

ans=0
adjacency={}

for q in queens:
    adjacency[q[2]]=[]
    from_neighbours(adjacency,q,grid)
    #print(adjacency)
ans=0

for q in queens:
    start=q[2]
    visited=set()
    ans=max(ans,find_max(q,grid,visited,adjacency))

print(M-ans+1)
            
"""
OUTPUT

Data8 9

Pass Data8,8,Q1

Pass Data8,5,Q2

Pass Data7,6,Q3

Pass Data6,3,Q4

Pass Data5,1,Q5

Pass Data3,3,Q6

Pass Data3,8,Q7

Pass Data2,7,Q8

Pass Data1,4,Q9


2
"""
              
            
    
            
            
            
            
            