#!/usr/bin/env python
# coding: utf-8

# In[3]:


# 0/1 Knapsack Recursive Code


def knapsack(W,val,wt,n,i):
    
    if i==n:
        return 0
    
    if wt[i]>W:
        ans = knapsack(W,val,wt,n,i+1)
        
    else:
        #inclusion of ith item
        ans1 = val[i]+knapsack(W-wt[i],val,wt,n,i+1)
        #exclusion of ith item
        ans2 = knapsack(W,val,wt,n,i+1)
        ans = max(ans1,ans2)
        
    return ans
    
    
val = [200,300,100]
wt = [20,25,30]
W = 50
n = len(val)
ans = knapsack(W,val,wt,n,0)
print(ans)


# In[8]:


# Knapsack Iterative

def knapsack(W,val,wt):
    n=len(val)
    dp=[[0 for j in range(W+1)]for i in range(n+1)]
    
    for i in range(1,n+1):
        for j in range(1,W+1):
            if j<wt[i-1]:
                ans=dp[i-1][j]
            else:
                ans1=val[i-1]+dp[i-1][j-wt[i-1]]
                ans2=dp[i-1][j]
                ans=max(ans1,ans2)
            dp[i][j]=ans
    return dp[n][W]

val=[200,300,100]
wt=[20,25,30]
W=50

ans=knapsack(W,val,wt)
print(ans)


# In[ ]:


import sys
def mcm(p,i,j):
    if i==j:
        return 0
    min_value=sys.maxsize
    for k in range(i,j):
            ans1=mcm(p,i,k)
        else:
            ans2=mcm(p,k+1,j)
        else:
            ans2=[k+1][j]
            
        mCost=p[i-1]*p[k]*p[j]
        curr_value=ans1+ans2+mCost
        min_value=min(min_value,curr_value)
    return min_value
p=[2,3,4,5,6]
n=len(p)-1
dp=[[-1 for j in range(n+1)]for i in range(n+1)]
ans=mcm(p,1,n,dp)
print(ans)


# In[17]:


#MCM Recurrence Relation

import sys
def mcm(p,i,j):
    if i==j:
        return 0
    
    min_value=sys.maxsize
    for k in range(i,j):
            ans1=mcm(p,i,k)
            ans2=mcm(p,k+1,j)
            
            mCost=p[i-1]*p[k]*p[j]
            curr_value=ans1+ans2+mCost
            min_value=min(min_value,curr_value)
    
    return min_value

p=[2,3,4,5,6]
n=len(p)-1
ans=mcm(p,1,n)
print(ans)


# In[18]:


#MCM Memoization

import sys
def mcm(p,i,j,dp):
    if i==j:
        return 0
    min_value=sys.maxsize
    for k in range(i,j):
        if dp[i][k]==-1:
            ans1=mcm(p,i,k,dp)
        else:
            ans1=dp[i][k]
        if dp[k+1][j]==-1:
            ans2=mcm(p,k+1,j,dp)
        else:
            ans2=dp[k+1][j]
            
        mCost=p[i-1]*p[k]*p[j]
        curr_value=ans1+ans2+mCost
        min_value=min(min_value,curr_value)
    return min_value
p=[2,3,4,5,6]
n=len(p)-1
dp=[[-1 for j in range(n+1)]for i in range(n+1)]
ans=mcm(p,1,n,dp)
print(ans)


# In[ ]:




