# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 13:27:41 2020

@author: kdban
"""
def count_for(a,b):
    min_side=min(a,b)
    max_side=max(a,b)
    
    if min_side==0:
        return 0
    if min_side==1:
        return a*b

    
    total=max_side//min_side
    new_side=max_side%min_side
    total=total+count_for(new_side,min_side)
    return total

T=int(input("Enter "))
for case in range(T):
    P,Q,R,S=list(map(int,input("Data").split()))
    ans=0
    for i in range(P,Q+1):
        for j in range(R,S+1):
            ans=ans+count_for(i,j)
            
    print(ans)
    

