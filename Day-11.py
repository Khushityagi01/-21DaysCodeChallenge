#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Return All Subsequences 

def subs(s):
    if len(s)==0:
        output=[]
        output.append("")
        return output
    
    smallerString =s[1:]
    smallerOutput = subs(smallerString)
    
    output=[]
    for sub in smallerOutput:
        output.append(sub)
        
    for sub in smallerOutput:
        subs_with_zeroth_char = s[0]+sub
        output.append(subs_with_zeroth_char)
        
    return output


# In[2]:


subs("abcd")


# In[3]:


def subsequences(string):
    
    if len(string) == 0:
        output = [""]
        return output
    
    smallOutput = subsequences(string[1:])
    output = []
    for s in smallOutput:
        output.append(s)
        output.append(string[0] + s)
    return output

string = input()
ans = subsequences(string)
for ele in ans:
    print(ele)


# In[4]:


#Return Keypad Combination

def getString(d):
    if d==2:
        return "abc"
    if d==3:
        return "def"
    if d==4:
        return "ghi"
    if d==5:
        return "jkl"
    if d==6:
        return "mno"
    if d==7:
        return "pqrs"
    if d==8:
        return "tuv"
    if d==9:
        return "wxyz"
    return ""


# In[5]:


def keypad(n):
    if n==0:
        output=[]
        output.append("")
        return output
    
    smallerNumber = n//10
    lastDigit = n%10
    
    
    smallerOutput = keypad(smallerNumber)
    optionsForLastDigit = getString(lastDigit)
    
    output = []
    
    for s in smallerOutput:
        for c in optionsForLastDigit:
            option = s+c
            output.append(option)
    return output


# In[6]:


keypad(23)


# In[7]:


output=keypad(237)
len(output),output


# In[8]:


#Print Output Instead of Returning

def factHelper(n):
    if n==0:
        return 1
    smallOutput=factHelper(n-1)
    output=n*smallOutput
    return output

def fact(n):
    output=factHelper(n)
    print(output)
fact(5)

def printFact(n,ans):
    if n==0:
        print(ans)
        return
    ans=ans*n
    printFact(n-1,ans)

printFact(5,1)


# In[9]:


#Minimum of Array

def minList(l):
    if len(l)==1:
        return l[0]
    
    minSmallArray=minList(l[1:])
    overallMin=min(minSmallArray,l[0])
    return overallMin

def printMin(l,minSoFar=100000):
    if len(l)==0:
        print(minSoFar)
        return
    newMin=min(minSoFar,l[0])
    printMin(l[1:],newMin)

printMin([1,2,3,4,-1,0,-2,-4,5,6])


# In[10]:


#Print All Subsequences

def printSubs(s,o):
    if len(s)==0:
        print(o)
        return
    
    #don't include 0th char
    printSubs(s[1:],o)
    
    #include 0th char
    newOutput = o + s[0]
    printSubs(s[1:],newOutput)


# In[11]:


printSubs("abc","")


# In[12]:


#Print Keypad Combination

def getString(d):
    if d==2:
        return "abc"
    if d==3:
        return "def"
    if d==4:
        return "ghi"
    if d==5:
        return "jkl"
    if d==6:
        return "mno"
    if d==7:
        return "pqrs"
    if d==8:
        return "tuv"
    if d==9:
        return "wxyz"
    return ""

def printkeypad(n,outputSoFar):
    if n==0:
        print(outputSoFar)
        return
    smallNumber=n//10
    lastDigit=n%10
    
    optionsForLastDigit=getString(lastDigit)
    for c in optionsForLastDigit:
        newOutput=c+outputSoFar
        printkeypad(smallNumber,newOutput)

printkeypad(23,"")


# In[ ]:




