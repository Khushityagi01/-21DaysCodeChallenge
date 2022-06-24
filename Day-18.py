#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


x = [1,2,3]
y = [2,4,6]

plt.scatter(x,y)
plt.show()


# In[3]:


x = [1,2,3]
y = [2,4,6]
plt.scatter(x,y)
plt.plot(x,y)


# In[4]:


x = [1,2,3]
y = [2,4,6]

x2 = [3,4,5]
y2 = [2,4,6]
plt.scatter(x2,y2)
plt.scatter(x,y)
plt.plot(x,y)
plt.plot(x2,y2,"g")


# In[5]:


#plot function x^3
import numpy as np
#x = np.array([1,2,3,4])
x = np.arange(0,5,0.1)
y = x**3
plt.plot(x,y,"go")


# In[6]:


a = [3,4,5]
plt.plot(a)


# In[7]:


#plot function x^3
import numpy as np
#x = np.array([1,2,3,4])
x = np.arange(0,5,0.1)
y = x**3
y2 = x**2
#plt.plot(x,y,color="black",marker="+")
plt.plot(x,y,color="black",linewidth=5,label="x^3")
plt.plot(x,y2,color="red",linewidth=5,label="x^2")
#plt.axis([0,10,0,200])

plt.grid()
plt.text(2,80,"Text",fontsize=12)
plt.ylabel("y")
plt.xlabel("x")
plt.legend()
plt.title("Matplotlib demo")
plt.show()


# In[8]:


#pie graphs

labels=["A","B","C","D"]
sizes = [3,4,6,2]
colors=["blue","purple","red","yellow"]
explode = [0.1,0,0,0]
plt.title("Split among classes")
plt.pie(sizes,colors=colors,labels=labels,explode=explode,autopct="%.2f%%",counterclock=False)
plt.axis("equal")
plt.show()


# In[ ]:




