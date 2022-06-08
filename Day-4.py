#!/usr/bin/env python
# coding: utf-8

# In[43]:


a = {}


# In[44]:


type(a)


# In[45]:


a  = {"the":1,"a":5,10000:"abc"}


# In[46]:


print(a)


# In[47]:


len(a)


# In[48]:


b= a.copy()


# In[49]:


b


# In[50]:


c=dict([{"the",3},{"a",10},{2,3}])


# In[51]:


c


# In[52]:


d = dict.fromkeys(["abc",32,])


# In[53]:


d


# In[54]:


a = {1:2,3:4,"list":[1,23],"dict":{1:2}}


# In[55]:


a


# In[56]:


a[1]


# In[57]:


a[3]


# In[58]:


a['list']


# In[59]:


a.get(1)


# In[60]:


a.get('list')


# In[61]:


a.keys()


# In[62]:


a.values()


# In[63]:


a.items()


# In[64]:


for i in a:
    print(i)


# In[65]:


for i in a:
    print(i,a[i])


# In[66]:


for i  in  a.values():
    print(i)


# In[67]:


"list" in a


# In[68]:


"li" in a


# In[69]:


2 in  a


# In[70]:


a


# In[71]:


a['t']=(1,2,3)


# In[72]:


a


# In[73]:


a[1] = 10


# In[74]:


a


# In[75]:


b = {3:5,'the':4,2:100}


# In[76]:


a.update(b)


# In[77]:


a


# In[78]:


a.pop('t')


# In[79]:


a


# In[80]:


del a[1]


# In[81]:


a


# In[82]:


a.clear()


# In[83]:


a


# In[84]:


del a


# In[88]:


a = {1:2,'list':[1,2],3:5}
b = {4:5,3:7}
a.update(b)


# In[89]:


a


# In[90]:


a = {1:2,'list':[1,2],3:5}
a.pop('list')


# In[91]:


a['list'] = [3,5]
print(a['list'])


# In[100]:


#Print All the words with frequency k

s = "This is a word string having many many word"
k=2


# In[101]:


words=s.split()


# In[102]:


words


# In[103]:


d = {}
for w in words:
    d[w]=d.get(w,0)+1


# In[104]:


d


# In[105]:


for w in d:
    if d[w]==k:
        print(w)


# In[106]:


def printKFreqWords(s,k):
    words = s.split()
    d = {}
    for w in words:
        d[w]=d.get(w,0)+1
    for w in d:
        if d[w]==k:
            print(w)

    
    


# In[109]:



printKFreqWords(s,2)


# In[112]:


#How to insert in Map

class MapNode:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None
class Map:
    
    def __init__(self):
        self.bucketSize=10
        self.buckets=[None for i in range(self.bucketSize)]
        self.count=0
        
    def size(self):
        return self.count
    
    def getBucketIndex(self,hc):
        return (abs(hc)%(self.bucketSize))
    
    def insert(self,key,value):
        hc=hash(key)
        index=self.getBucketIndex(hc)
        head=self.buckets[index]
        while head is not None:
            if head.key==key:
                head.value=value
                return
            head=head.next
        newNode=MapNode(key,value)
        newNode.next=head
        self.buckets[index]=newNode
        self.count+=1

m=Map()
m.insert('Parikh',2)
print(m.size())
m.insert('Rohan',7)
print(m.size())
m.insert('Parikh',9)
print(m.size())
    


# In[110]:


class MapNode:
    def __init__ (self,key,value):
        self.key = key #to store key
        self.value = value #to store value
        self.next = None #to the next pointer

class Map:
    def __init__ (self):
        self.bucketSize = 10#Buckets for compression function
        # Store the head pointers
        self.buckets = [None for i in range(self.bucketSize)]
        self.count = 0 #To store the size
    def size(self):#Return the size of the map
        return self.count
    def getBucketIndex(self,hc):#Index using hash function
        return (abs(hc)%(self.bucketSize))
    def insert(self,key,value):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.buckets[index]
        while head is not None:
            if head.key == key:
                head.value = value
                return
        head = head.next
        newNode = MapNode(key,value)
        newNode.next = head
        self.buckets[index] = newNode
        self.count+=1


# In[113]:


m=Map()
m.insert('Parikh',2)
print(m.size())
m.insert('Rohan',7)
print(m.size())
m.insert('Parikh',9)
print(m.size())
    


# In[ ]:




