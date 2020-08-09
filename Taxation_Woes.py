# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 10:48:51 2020

@author: Kuldeep
"""

#import math
slabs=list(map(int,input("Data").split()))
tax_rate=list(map(int,input("Tax").split()))
rebate=int(input("Rebate"))
tax_paid=list(map(int,input("Data").split()))
num_employees=len(tax_paid)
salaries=[0]*num_employees
for i in range(num_employees):
    paid_by_curr_employee=tax_paid[i]  
    salaries[i]+=slabs[0]
    for j in range(1,len(slabs)):
        max_curr_slab=tax_rate[j-1]*(slabs[j]-slabs[j-1])/100
        if max_curr_slab<=paid_by_curr_employee:
            salaries[i]+= (slabs[j]-slabs[j-1])
            paid_by_curr_employee-= max_curr_slab
        else:
            paid_in_slab=((paid_by_curr_employee*100)/tax_rate[j-1])
            salaries[i]=salaries[i]+paid_in_slab
            paid_by_curr_employee=paid_by_curr_employee-paid_in_slab
        
    if paid_by_curr_employee>0:
        salaries[i]=salaries[i]+((paid_by_curr_employee*100)/tax_rate[-1])
    salaries[i]=salaries[i]+rebate
    salaries[i]=int(salaries[i])
ans=sum(salaries)
print(ans)

"""
INPUT Format

300000 600000 900000
10 20 30
100000
900000 150000 210000 300000


"""



