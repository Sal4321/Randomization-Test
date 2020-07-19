# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 22:05:39 2020

@author: Salehin
"""
from itertools import combinations
import math
import numpy as np
data=[6,8,9,11,9,17,15,16,16]
indexes=list(range(1,len(data)+1))
import random
sizea=2
sizeb=3
sizec=4
def removefroma(indexes,trta):
    b=[]
    for i in range(len(indexes)):
        k=indexes[i]
        if k not in trta:
            b.append(k)
    return b      
def randomselection(size,array):
    current=[]
    new=array
    for i in range(size):
        a=random.choice(new)
        if a not in current:
            current.append(a)
            new.remove(a)
    return current        
            
   

def stats(index,data):
    summ=0
    for i in range(len(index)):
        summ+=data[index[i]-1]
    return summ**2/len(index)   


def trta(indexes,sizea):
     return list(combinations(indexes,sizea))  
removable=()
n=0
p=0
storage=np.zeros([1260,10])
original=stats((1,2),data)+stats((3,4,5),data)+stats((6,7,8,9),data)
for i in range(int(math.factorial(len(indexes))/((math.factorial(sizea))*math.factorial(len(indexes)-sizea)))):
    currenta=trta(indexes,sizea)[i]
    removable=currenta
    other=removefroma(indexes,removable)
    treatmentb=trta(other,sizeb)
    for j in range(len(treatmentb)):
        currentb=treatmentb[j]
        removable=removable+currentb
        other=removefroma(indexes,removable)
        removable=currenta
        total=stats(currenta,data)+stats(currentb,data)+stats(other,data)
        a=[currenta[0],currenta[1],currentb[0],currentb[1],currentb[2],other[0],other[1],other[2],other[3],total]
        storage[n][0],storage[n][1]=currenta[0],currenta[1]
        storage[n][2],storage[n][3],storage[n][4]=currentb[0],currentb[1],currentb[2]
        storage[n][5],storage[n][6],storage[n][7],storage[n][8]=other[0],other[1],other[2],other[3]
        storage[n][9]=total
        if(total>=original):
            p+=1
        n+=1    
        

np.savetxt('result.txt',storage,delimiter=',',fmt='%1d')       
print("Result with Systematic Permutation: ",p/n)
n=800
p1=0
r=np.zeros([800,9])
for i in range(n-1):
    currentarray=indexes.copy()
    trta=randomselection(sizea,currentarray)
    
    arraytoremove=trta
    currentarray=removefroma(indexes,arraytoremove)
    trtb=randomselection(sizeb,currentarray)
    arraytoremove=trta+trtb
    currentarray=removefroma(indexes,arraytoremove)
    trtc=currentarray.copy()
    total=stats(trta,data)+stats(trtb,data)+stats(trtc,data)
    r[i][0],r[i][1],r[i][2],r[i][3],r[i][4],r[i][5],r[i][6],r[i][7],r[i][8]=trta[0],trta[1],trtb[0],trtb[1],trtb[2],trtc[0],trtc[1],trtc[2],trtc[3]
    if(total>=original):
        p1+=1
    currentarray.clear()
    arraytoremove.clear()  
np.savetxt('random.txt',r,delimiter=',',fmt='%1d')    
print('Result with random permutation: ',p1/n)    
        
    
    

    
    
        
    

       

    
    
        
            
         
            
        