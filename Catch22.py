# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 18:12:18 2020

@author: kdban
"""
from math import inf
def solve(F,B,T,FD,BD):
    if FD<=F:
        return FD, "F"

    if BD<=B-F:
        return F+F+BD,"B"
    
    if F==B:
        return inf, None
    if F-B>0:
        meters=0
        df=F-B
        distPerStep=F+B
        if((FD-F)%df)==0:
            numFullsteps=(FD-F)//df
            meters +=numFullsteps*distPerStep+F
        
        else:
            numFullsteps=(FD-F)//df+1
            remainingDist=FD-numFullsteps*df
            meters += numFullsteps*distPerStep+remainingDist
            
        return meters,"F"
    if B-F>=0:
        return meters,"B"
        
        pass
    

if __name__=="__main__":
    N=int(input("Enter Test Data:"))
    
    for i in range(N):
        F,B,T,FD,BD=[int(x) for x in input("Enter:").strip().split()]
        dist,direction=solve(F,B,T,FD,BD)
        time=dist*T
        if time==inf:
            print("No Ditch")
        else:
            print(f"{time} {direction}")


