# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 09:58:35 2020

@author: kdban
"""

def solve(N,Q,X):
    sortedQ=sorted(Q)
    for i in range(N-2):
        for j in range(1,N-1):
            for k in range(2,N):
                if i==j or i==k or j==k:
                    continue
                    
                if sortedQ[i]+sortedQ[j]+sortedQ[k]==X:
                    return True
    return False


if __name__=="__main__":
    N=int(input("Enter Data"))
    Q=[int(input("Value")) for _ in range(N)]
    X=int(input("X:"))
    
    print(solve(N,Q,X))
     


