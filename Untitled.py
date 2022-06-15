#!/usr/bin/env python
# coding: utf-8

# In[1]:


#LCS Recursive

def lcs(str1,str2,i,j):
    
    if i==len(str1) or j==len(str2):
        return 0
    
    if str1[i]==str2[j]:
        ans = 1+lcs(str1,str2,i+1,j+1)
        
    else:
        ans1 = lcs(str1,str2,i+1,j)
        ans2 = lcs(str1,str2,i,j+1)
        ans = max(ans1,ans2)
        
        
    return ans
    

str1 = "abedgjc"
str2 = "bmdgsc"
ans = lcs(str1,str2,0,0)
print(ans)


# In[2]:


#LCS Memoization



def lcs(str1,str2,i,j,dp):
    
    if i==len(str1) or j==len(str2):
        return 0
    
    if str1[i]==str2[j]:
        if dp[i+1][j]==-1:
            smallAns = lcs(str1,str2,i+1,j+1,dp)
            dp[i+1][j]=smallAns
            ans = 1+smallAns
        else:
            ans=1+dp[i+1][j+1]
        
    else:
        if dp[i+1][j]==-1:
            ans1 = lcs(str1,str2,i+1,j,dp)
            dp[i+1][j]=ans1
            
        else:
            ans1 = dp[i+1][j]
            
        if dp[i][j+1]==-1:
            ans2 = lcs(str1,str2,i,j+1,dp)
            dp[i][j+1]=ans2
        else:
            ans2 = dp[i][j+1]
        ans = max(ans1,ans2)
        
        
    return ans


str1="abedgjc"
str2="bmdgsc"
n=len(str1)
m=len(str2)
dp=[[-1 for j in range(m+1)]for i in range(n+1)]
ans=lcs(str1,str2,0,0,dp)
print(ans)


# In[3]:


#LCS Iterative

def lcs(str1,str2):
    n=len(str1)
    m=len(str2)
    dp=[[0 for j in range(m+1)]for i in range(n+1)]
    
    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            if str1[i]==str2[j]:
                dp[i][j]=1+dp[i+1][j+1]
            else:
                dp[i][j]=max(dp[i+1][j],dp[i][j+1])
    return dp[0][0]

str1="abedgjc"
str2="bmdgsc"


ans=lcs(str1,str2)
print(ans)


# In[ ]:




