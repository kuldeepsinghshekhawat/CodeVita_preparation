# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 16:58:06 2020

@author: Kuldeep Singh

Topic: Supreme Contest marathon Winner
"""

N=int(input("N"))
T=int(input("T"))


steps={}
step_size={}
distances={}
max_distances={}
leading_positions={}

for participant in range(1,N+1):
    steps[participant]=list(map(int,input("Data").split()))
    step_size[participant]=steps[participant][-1]
    steps[participant]=steps[participant][:-1]
    
    for position in range(T):
        if position==0:
            distances[participant]=[steps[participant][0]*step_size[participant]]
        else:
            prev=distances[participant][position-1]
            distances[participant].append(prev+(step_size[participant]*steps[participant][position]))
            
        if position in max_distances:
            max_distances[position]=max(distances[participant][position],max_distances[position])
        
        else:
            max_distances[position]=distances[participant][position]
            
all_participants=[i for i in range(1,N+1)]
for position in range(1,T,2):
    curr_max_distances=max_distances[position]
    for participant in range(1,N+1):
        if distances[participant][position]==curr_max_distances:
            if participant in leading_positions:
                leading_positions[participant]+= 1
            else:
                leading_positions[participant]=1

winner=N+100
max_wins=-1
for participant in leading_positions:
    if leading_positions[participant]>max_wins:
        winner=participant
        max_wins=leading_positions[participant]
    elif leading_positions[participant]==max_wins and participant < winner:
        winner=participant
        max_wins=leading_positions[participant]
print(winner)







"""
INPUT FORMAT

3
8
2 2 4 3 5 2 6 2 3
3 5 7 4 3 9 3 2 2  
1 2 4 2 7 5 3 2 4

OUTPUT
2
"""
