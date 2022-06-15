#!/usr/bin/env python
# coding: utf-8

# In[1]:


#MinCost Path Recursively

import sys
def minCost(cost,i,j,n,m):
    
    #Special Case
    if i==n-1 and j==m-1:
        return cost[i][j]
    
    
    #Base Case
    if i>=n or j>=m:
        return sys.maxsize
    
    
    ans1 = minCost(cost,i,j+1,n,m)
    ans2 = minCost(cost,i+1,j,n,m)
    ans3 = minCost(cost,i+1,j+1,n,m)
    
    
    ans = cost[i][j]+min(ans1,ans2,ans3)
    return ans


cost = [[1,5,11],[8,13,12],[2,3,7],[15,16,18]]
ans = minCost(cost,0,0,4,3)
print(ans)


# In[2]:


#MinCost Memoization
# Time complexity:0(m+1,n+1)
# Space complexity:0(m+1,n+1)



import sys
def minCost(cost,i,j,n,m,dp):
    
    #Special Case
    if i==n-1 and j==m-1:
        return cost[i][j]
    
    
    #Base Case
    if i>=n or j>=m:
        return sys.maxsize
    
    if dp[i][j+1]==sys.maxsize:
        ans1 = minCost(cost,i,j+1,n,m,dp)
        dp[i][j+1] = ans1
    else:
        ans1 = dp[i][j]+1
    
    if dp[i+1][j]==sys.maxsize:
        ans2 = minCost(cost,i+1,j,n,m,dp)
        dp[i+1][j] = ans2
    else:
        ans2 = dp[i+1][j]
        
        
    if dp[i+1][j+1]==sys.maxsize:
        ans3 = minCost(cost,i+1,j+1,n,m,dp)
        dp[i+1][j+1]=ans3
    
    else:
        ans3 = dp[i+1][j+1]
    
    
    ans = cost[i][j]+min(ans1,ans2,ans3)
    return ans


cost = [[1,5,11],[8,13,12],[2,3,7],[15,16,18]]
n=4
m=3
dp=[[ sys.maxsize for j in range(m+1)]for i in range(n+1)]
ans = minCost(cost,0,0,4,3,dp)
print(ans)


# In[3]:


#MinCost Iteratively

import sys

def minCostIterative(cost,n,m):
    
    dp = [[sys.maxsize for j in range(m+1)]for i in range(n+1)]
    
    
    
    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            if i==n-1 and j==m-1:
                dp[i][j] = cost[i][j]
            else:
                ans1 = dp[i+1][j]
                ans2 = dp[i][j+1]
                ans3 = dp[i+1][j+1]
                dp[i][j] = cost[i][j]+min(ans1,ans2,ans3)
                
    return dp[0][0]
                
                
cost = [[1,5,11],[8,13,12],[2,3,7],[15,16,18]]
n=4
m=3
ans = minCostIterative(cost,n,m)
print(ans)


# In[ ]:




