# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 16:49:35 2020

@author: kdban
"""

T=int(input("Test cases"))
for case in range(T):
    N=int(input("Data"))
    hours=[0]*(N+1)
    time_taken=0
    indegrees=[0]*(N+1)
    timeline=[0]*(N+1)
    edges=[]
    for e in range(N+1):
        edges.append([])#[[],[],[]]
    for m in range(1,N+1):
        inp=input("Module id")  
        inp=list(map(int,inp.split()))
        module_id=inp[0]
        hours[module_id]=inp[1]
        for dependency in inp[2:]:
            if(dependency>0):
                edges[dependency].append(module_id)
                indegrees[module_id]+= 1
                
    q=[]
    for m in range(1,N+1):
        if(indegrees[m]==0):
            q.append(m)#adding list dependent elements in queue
    
    while(len(q)>0):
        curr_node=q.pop(0)
        #update time
        timeline[curr_node]=hours[curr_node]+timeline[curr_node]
        for neighbour in edges[curr_node]:
            indegrees[neighbour]=indegrees[neighbour]-1
            timeline[neighbour]=max(timeline[neighbour],timeline[curr_node])
            if(indegrees[neighbour]==0):
                q.append(neighbour)
    time_taken=max(timeline)
    print(time_taken)
    #print(edges)
    #print(dependency)
    
        
        
        