# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 16:00:25 2020

@author: Salehin
"""

data=[6,8,9,11,9,17,15,16,16]
indexes=list(range(1,len(data)+1))
def lasttreatment(a,index):
    last=[]
    for i in index:
        if i not in a:
           last.append(i)
    return last       
def trta(a,sizea):
    trta=[]
    for i in range(sizea):
        trta.append(a[i])
    return trta   

def trtb(a,sizea,sizeb):
    trtb=[]
    for i in range(sizea,sizea+sizeb):
        trtb.append(a[i])
    return trtb

        
        
  

def stats(d,data,sizea,sizeb,sizec):
        c=lasttreatment(d,indexes)
        a=trta(d,sizea)
        b=trtb(d,sizea,sizeb)
        sumc,suma,sumb=0,0,0
        for i in range(len(c)):
            sumc+=data[c[i]-1]
        for i in range(len(a)):
            suma+=data[a[i]-1]
        for i in range(len(b)):
            sumb+=data[b[i]-1]    
        x=sumc**2/sizec
        y=sumb**2/sizeb
        z=suma**2/sizea
        return z+y+x
    
print(stats((1,2,3,4,5),data,2,3,4))    
        
        
def giver1(i,j):
    for x in range(1,10):
        if(x!=i and x!=j):
            return x
    return 0    

def giver2(i,j,k):
    for x in range(1,10):
        if(x!=i and x!=j and x!=k):
            return x
    return 0 

def giver3(i,j,k,l):
    for x in range(1,10):
        if(x!=i and x!=j and x!=k and x!=l):
            return x
    return 0     

def sameornot(i,j,k,l,m):
    if(i==j or i==k or i==l or i==m):
        return 1
    if(j==k or j==l or j==m):
        return 1
    if(k==l or k==m):
        return 1
    if(l==m):
        return 1
    else:
        return 0
        
     
original=stats([1,2,3,4,5],data,2,3,4)    
print(original)
n=0
d=[]
for i in range(1,9):
    for j in range(i+1,10):
        x=giver1(i,j)
        y=giver2(i,j,x)
        z=giver3(i,j,x,y)
        for k in range(x,8):
            for l in range(y,9):
                for m in range(z,10):
                    if(l>k and m>l) and sameornot(i,j,k,l,m)==0:
                        d.append((i,j,k,l,m))
                        n+=1
p=0                        
for i in range(len(d)):
    s=d[i]
    print(stats(s,data,2,3,4))
    if(stats(s,data,2,3,4)>=original):
        p+=1
print(p/n)        
                            
                    
                    
print(n)                    