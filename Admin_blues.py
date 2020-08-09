# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 16:14:19 2020

@author: Kuldeep Singh Shekhawat


"""
def is_consonant(alpha):
    if alpha not in "aeiou":
        return True
    return False

def possibilities(curr_string,remaining_employees,curr_users):
    ans=0
    if len(curr_string)==0 and remaining_employees==0:
        return 1
    if len(curr_string)<4:
        return ans
    
    start=0
    end=start+3
    for i in range(end,len(curr_string)):
        curr_user_id=curr_string[start:i+1]
        if is_consonant(curr_string[start]) and is_consonant(curr_string[i])  and curr_user_id not in curr_users:
            curr_users.add(curr_user_id)
            ans=ans+possibilities(curr_string[i+1:],remaining_employees-1,curr_users)
            curr_users.remove(curr_user_id)
    
    return ans

num_employees=int(input("Emp"))
full_string=input("String")
curr_users=set()

ans=possibilities(full_string,num_employees,curr_users)

print(ans)



"""
INPUT FORMAT

Emp2

Stringnonajklop
1
"""