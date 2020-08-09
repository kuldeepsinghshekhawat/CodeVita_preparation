# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 14:12:06 2020

@author: Kuldeep Singh
It is based on LCM
"""
import math
def lcm(nums):
    a=nums[0]
    b=nums[1]
    curr_lcm=a*b//(math.gcd(a,b))
    for num in nums[2:]:
        curr_lcm=(curr_lcm*num)//(math.gcd(num,curr_lcm))
    return curr_lcm


try:
    N=int(input("Test Cases:"))
    N=N//2
    point_dict={"Darrell":0,"Sally":0}
    for case in range(N):
        question_input=input("Data:")
        question_input=question_input.split()
        questioner=question_input[0]
        nums_str=question_input[1]
        
        nums=list(map(int,nums_str.split(",")))
        assert(2<=len(nums)<=7)
        for num in nums:
            assert(1<=num<=100)
        print(f"{questioner}'s question is:{nums_str}")
        answer_input=input().split()
        answerer=answer_input[1]
        if case==0:
            first=questioner
            second=answerer
        correct_answer=lcm(nums)
        if answer_input[2] !='pass':
            ans=int(answer_input[2])
            if ans==correct_answer:
                print("Correct answer")
                print(f'{answer}:10points')
                point_dict[answerer]=point_dict[answerer]+10
            else:
                print("Incorrect answer")
                print(f'{answer}:0points')
        else:
            print("Question is passed")
            correct_answer=0
            print(f'Answer is: {correct answer}')
            print(f'{answer}:0points')
        #ans=answer_input[2]
        #print(answerer,ans)
        if case==N-1:
            print("Total Points")
            print(f'{first}:{point_dict[first]}points')
            print(f'{second}:{point_dict[second]}points')
            if point_dict["Darrell"]==point_dict["Sally"]:
                print("Game Result: Draw")
            elif point_dict["Darrell"] > point_dict["Sally"]:
                print("Game result: Darrell  is winner")
            else:
                print("Game Result: Sally  is winner")
                
except:
    print("Invalid input")
#Darrell:0points
#Sally:10points



