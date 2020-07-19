# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 21:42:24 2020

@author: Salehin
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 16:12:42 2020

@author: Salehin
"""

from itertools import permutations
import numpy as np
import math

data=[6,8,9,11,9,17,15,16,16]
sizea=2
sizeb=3
sizec=4
total=math.factorial(len(data))/(math.factorial(sizea)*math.factorial(sizeb)*math.factorial(sizec))
def stats(size1,size2,size3,data):
    sum1,sum2,sum3=0,0,0
    for i in range(size1):
        sum1+=data[i]
    for i in range(sizeb):
        sum2+=data[i+size1]
    for i in range(sizec):
        sum3+=data[i+size1+size2]
    return ((sum1**2/sizea)+(sum2**2/sizeb)+(sum3**2/sizec)) 

perm1=list(permutations(data))

print(stats(sizea,sizeb,sizec,perm1[25]))
#
#

#
##print("Here are the test statistics ")
#p=0
#for i in range(len(perm1)):
    
                

#print("The p value is",p/1260)
                   
            


    
    
    
    
       
        
        
        
        
    