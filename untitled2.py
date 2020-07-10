# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 13:17:28 2020

@author: kdban
program: string rotation
"""
if __name__=="__main__":
    word=input("Enter word:").strip()
    first_char=[]
    idx=0# index of first char of the sting
    
    q=int(input("Enter"))
    for _ in range(q):#no. of rotations
        direc,s=input().strip().split()#L2 ==>>["L","2"]
        s=int(s)
        if direc=="L":
            idx=(idx+s) % len(word)
        else:
            idx=(idx-s) % len(word)
        
    
    