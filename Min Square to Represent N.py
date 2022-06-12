#!/usr/bin/env python
# coding: utf-8

# In[1]:


#By Recursive method
import math,sys

def minSquares(n):
    if n==0:
        return 0
    
    ans=sys.maxsize
    root=int(math.sqrt(n))
    for i in range(1,root+1):
        currAns=1+minSquares(n-(i**2))
        ans=min(ans,currAns)
    return ans
n=int(input())
ans=minSquares(n)
print(ans)


# In[2]:


#By Memorization method

import math,sys
def minSquares(n,dp):
    if n==0:
        return 0
    
    ans = sys.maxsize
    root = int(math.sqrt(n))
    for i in range(1,root+1):
        
        
        newCheckValue = n-(i**2)
        if dp[newCheckValue]==-1:
            smallAns = minSquares(newCheckValue,dp)
            dp[newCheckValue] = smallAns
            currAns=1+smallAns
        else:
            currAns = 1+dp[newCheckValue]
        
        ans = min(ans,currAns)
    return ans

n = int(input())
dp = [-1 for i in range(n+1)]
ans=minSquares(n,dp)
print(ans)


# In[3]:


#By iteratively method

import sys,math
def minSquaresI(n):
    dp=[-1 for i in range(n+1)]
    dp[0]=0
    
    for i in range(1,n+1):
        ans=sys.maxsize
        root=int(math.sqrt(i))
        for j in range(1,root+1):
            currAns=1+dp[i-(j**2)]
            ans=min(ans,currAns)
        dp[i]=ans
    return dp[n]

n=int(input())
ans=minSquaresI(n)
print(ans)


# In[ ]:




