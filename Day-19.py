#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


data = np.loadtxt("data.csv",delimiter=",")


# In[3]:


x = data[:,0]
y = data[:,1]


# In[4]:


x.shape


# In[5]:


from sklearn import model_selection
X_train,X_test,Y_train,Y_test=model_selection.train_test_split(x,y,test_size=0.3)


# In[6]:


X_train.shape


# In[7]:


def fit(x_train,y_train):
    num = (x_train*y_train).mean()-x_train.mean()*y_train.mean()
    den = (x_train**2).mean()-x_train.mean()**2
    m = num/den
    c = y_train.mean()-m*x_train.mean()
    return m,c


# In[8]:


def predict(x,m,c):
    return m*x+c

def score(y_truth,y_pred):
    u = ((y_truth-y_pred)**2).sum()
    v = ((y_truth-y_truth.mean())**2).sum()
    return 1-u/v

def cost (x,y,m,c):
    return ((y-m*x-c)**2).mean()
    


# In[9]:


m,c = fit(X_train,Y_train)
#test data
y_test_pred = predict(X_test,m,c)
print("Test score:",score(Y_test,y_test_pred))

#train data
y_train_pred = predict(X_train,m,c)
print("Train Score: ",score(Y_train,y_train_pred))
print("M,C",m,c)
print("Cost on training data",cost(X_train,Y_train,m,c))


# In[ ]:





# In[ ]:




