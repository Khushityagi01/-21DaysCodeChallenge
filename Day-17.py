#!/usr/bin/env python
# coding: utf-8

# In[1]:


list1 = list()


# In[2]:


list1


# In[3]:


list1 = list([1,2,3])


# In[4]:


list1


# In[5]:


mylist=list("hello")


# In[6]:


mylist


# In[7]:


len(mylist)


# In[8]:


list1 = [2445,133,12454,123]
max(list1)


# In[9]:


print([i.lower() for i in "HELLO"])


# In[10]:


d = {"john":40, "peter":45}
"john" in d


# In[11]:


l=[[1,2,3],[4,5,6]]
print(l)
l[0][1]


# In[12]:


import math as m
m.sqrt(20)


# In[13]:


import numpy as np


# In[14]:


l = [1,2,3]
np.array(l)

a =np.zeros(10)
a.dtype
np.zeros((2,3))


# In[15]:


np.arange(10)


# In[16]:


a = np.array([0, 1, 2, 3])
a.shape


# In[17]:


a = np.array([1,2,3])
b = np.array([5,6,7])

print(a+b)
print(a-b)
print(a*2)
print(a*b)


# In[18]:


a.mean()


# In[19]:


a.sum()


# In[20]:


a = np.array([5, 1, 2, 1])
a.mean()


# In[21]:


a = np.array([0, 1, 2, 3])
b = np.array([2, 3, 4, 5])
a.dot(b)


# In[22]:


a = np.matrix('1 2 4; 3 4 5')
a.shape


# In[23]:


np.sum([[0, 1], [0, 5]], axis=1)


# In[24]:


import pandas as pd 
iris =   pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
print(type(iris))


# In[25]:


iris


# In[26]:


iris.isnull().sum()


# In[27]:


iris.sum()


# In[28]:


df= iris.copy()


# In[29]:


df.head()


# In[30]:


df.head(10)


# In[31]:


print(df.shape)


# In[32]:


df.columns = ['sl','sw', 'pl','pw','flower_type']


# In[33]:


print(df.shape)
print(df.dtypes)


# In[34]:


df.describe()


# In[35]:


df.isnull()


# In[36]:


df.isnull().sum()


# In[37]:


df.iloc[1:4,2:3]


# In[38]:


df.iloc[1:3,:2]


# In[39]:


import pandas as pd   
iris=pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
iris.drop(0)
print(iris)


# In[40]:


iris.head()


# In[41]:


import pandas as pd   
iris=pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
iris.drop(0,inplace=True)
print(iris)


# In[42]:


iris


# In[43]:


iris.head()


# In[ ]:


import pandas as pd   
iris=pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
iris.drop(0,inplace= True)
iris.drop(0,inplace= True)
print(iris)


# In[ ]:


df.index


# In[ ]:


df[df.sl>3]


# In[ ]:


df[df.flower_type=='Iris-setosa'].describe()


# In[ ]:


print(df.head())
df.iloc[0]


# In[ ]:


df.loc[149] = [1,2,3,4,"Iris-setosa"]


# In[ ]:


df.head()


# In[ ]:


df.tail()


# In[ ]:


df.index


# In[ ]:


df.drop('sl',axis=1,inplace=True)


# In[ ]:


df.describe()


# In[ ]:


del df['sw']


# In[ ]:


df.describe()


# In[ ]:


df.head()


# In[ ]:


df = iris.copy()
df.columns = ['sl','sw','pl','pw','flower_type']
df.describe()


# In[ ]:


df.tail()


# In[ ]:


df["diff_pl_pw"] =  df["pl"] - df["pw"]
df.tail()


# In[ ]:


df.iloc[2:4,1:3] = np.nan
df.head()


# In[ ]:


df.describe()


# In[ ]:


df.dropna(inplace=True)


# In[ ]:


df.head()


# In[ ]:


df.reset_index(drop=True,inplace=True)


# In[ ]:


df.head()


# In[ ]:


df.iloc[2:4,1:3] = np.nan
df.head()


# In[ ]:


df.sw.fillna(df.sw.mean(),inplace=True)
df.pl.fillna(df.pl.mean(),inplace=True)


# In[ ]:


df.head()


# In[ ]:


#string based data
df["Gender"] = "Female"
df.iloc[0:10,6]= "Male"


# In[ ]:


df.head()


# In[ ]:


df.tail()


# In[ ]:


def f(s):
    if s=="Male":
        return 0
    else:
        return 1
df["sex"]=df.Gender.apply(f)
df.head()


# In[ ]:


df.tail()


# In[ ]:


del df["Gender"]


# In[ ]:


df.head()


# In[ ]:




