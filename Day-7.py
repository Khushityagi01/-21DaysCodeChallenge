#!/usr/bin/env python
# coding: utf-8

# In[6]:


def fibb(n,dp):
    
    if n==0 or n==1:
        return n 
    
    if dp[n-1]==-1:
        ans1 = fibb(n-1,dp)
        dp[n-1] = ans1
    else:
        ans1 = dp[n-1]
    
    if dp[n-2]==-1:
        ans2 = fibb(n-2,dp)
        dp[n-2]= ans2
    else:
        ans2=dp[n-2]
        
    myAns = ans1 + ans2
    return myAns

n = int(input())
dp = [-1 for i in range(n+1)]
ans = fibb(n,dp)
print(ans)

#Time complexity-o(N)
#Space Complexity-o(N)


# In[8]:


def fibb(n,dp):
    
    if n==0 or n==1:
        return n
    if dp[n-1]==-1:
        ans1=fibb(n-1,dp)
        dp[n-1]=ans1
    else:
        ans1=dp[n-1]
        
    if dp[n-2]==-1:
        ans2=fibb(n-2,dp)
        dp[n-2]=ans2
    else:
        ans2=dp[n-2]
    
    myAns=ans1+ans2
    return myAns

def fibbI(n):
    dp=[0 for i in range(n+1)]
    dp[0] = 0
    dp[1] = 1
    i = 2
    while i<=n:
        dp[i] = dp[i-1]+dp[i-2]
        i+=1
    return dp[n]

n= int(input())
ans = fibbI(n)
print(ans)


# In[16]:


#Min Steps To 1

import sys
def minStepsTo1(n,dp):
    if n==1:
        return 0
    ans1=sys.maxsize
    if n% 3==0:
        if dp[n//3]==-1:
            ans1=minStepsTo1(n//3,dp)
            dp[n//3]=ans1
        else:
            ans1=dp[n//3]
    ans2=sys.maxsize
    
    if n%2==0:
        if dp[n//2]==-1:
            ans2=minStepsTo1(n//2,dp)
            dp[n//2]=ans2
        else:
            ans2=dp[n//2]
    if dp[n-1]==-1:
        ans3=minStepsTo1(n-1,dp)
        dp[n-1]=ans3
    else:
        ans3=dp[n-1]
        
    
    
    ans=1+min(ans1,ans2,ans3)
    return ans
n=int(input())
dp=[-1 for i in range(n+1)]
ans=minStepsTo1(n,dp)
print(ans)


# In[ ]:




