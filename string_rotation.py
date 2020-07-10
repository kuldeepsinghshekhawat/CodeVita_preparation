# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 19:04:57 2020

@author: kdban
program: string rotation
"""
def areCountsEqual(C1,C2):
    for k in C1:
        if k not in C2 or C1[k] !=C2[k]:
            return False
    return True


def getCharCounts(s):
    counts=dict()
    for char in s:
        if char not in counts:
            counts[char]=1
        else:
            counts[char] += 1
    return counts

def isAnagramSubstring(A,B):
    if len(A)<len(B):
        return False
    countB=getCharCounts(B)
    for i in range(0,len(A)-len(B)+1):
        window=A[i:i+len(B)]
        countWindow=getCharCounts(window)
        
        if areCountsEqual(countB,countWindow):
            return True

#"carrace" "rcr"
        #0=car
        #1=arr
        #2=rra
        #3=rac
        #4=ace


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
        
        first_char.append(word[idx])
        
    if isAnagramSubstring(word,first_char):
        print("YES")
    else:
        print("NO")