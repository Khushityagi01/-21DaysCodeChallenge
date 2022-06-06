#!/usr/bin/env python
# coding: utf-8

# In[6]:


class BinaryTreeNode:
    def __init__(self,data):
        self.data=data;
        self.left=None
        self.right=None


# In[7]:


def search(root,x):
    if root==None:
        return False
    if root.data==x:
        return True
    elif root.data>x:
        return search(root.left,x)
    else:
        return search(root.right,x)


# In[8]:


def printBetweenK1K2(root,k1,k2):
    if root==None:
        return
    if root.data>k2:
        printBetweenK1K2(root.left,k1,k2)
    elif root.data<k1:
        printBetweenK1K2(root.right,k1,k2)
    else:
        print(root.data)
        printBetweenK1K2(root.left,k1,k2)
        printBetweenK1K2(root.right,k1,k2)


# In[9]:


def printTreeDetailed(root):
    if root==None:
        return
    print(root.data,end=":")
    if root.left!=None:
        print("L",root.left.data,end=",")
    if root.right!=None:
        print("R",root.right.data,end="")
    print()
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)

import queue
def takeTreeInputLevelWise():
    q=queue.Queue()
    print("Enter root")
    rootData=int(input())
    if rootData==-1:
        return None
    root=BinaryTreeNode(rootData)
    q.put(root)
    while(not(q.empty())):
        current_node=q.get()
        print("Enter left child of",current_node.data)
        leftChildData=int(input())
        if leftChildData!=-1:
            leftChild=BinaryTreeNode(leftChildData)
            current_node.left=leftChild
            q.put(leftChild)
        print("Enter right child of",current_node.data)
        rightChildData=int(input())
        if rightChildData!=-1:
            rightChild=BinaryTreeNode(rightChildData)
            current_node.right=rightChild
            q.put(rightChild)
    return root


# In[25]:


def nodeToRootPath(root,s):
    if root==None:
        return None
    if root.data==s:
        l = list()
        l.append(root.data)
        return l
    
    leftouput = nodeToRootPath(root.left,s)
    if leftouput!=None:
        leftouput.append(root.data)
        return leftouput
    
    rightoutput = nodeToRootPath(root.right,s)
    if rightoutput!=None:
        rightoutput.append(root.data)
        return rightoutput
    else:
        return None
        
        


# In[17]:


def minTree(root):
    if root==None:
        return 100000
    leftMin = minTree(root.left)
    rightMin = minTree(root.right)
    return min(leftMin,rightMin,root.data)


# In[18]:


def maxTree(root):
    if root==None:
        return -100000
    leftMax = maxTree(root.left)
    rightMax = maxTree(root.right)
    return max(leftMax,rightMax,root.data)


# In[19]:


def isBST(root):
    if root==None:
        return True
    
    leftMax = maxTree(root.left)
    rightMin = minTree(root.right)
    if root.data > rightMin or root.data<=leftMax:
        return False
    
    isLeftBST = isBST(root.left)
    isRightBST = isBST(root.right)
    return isLeftBST and isRightBST
    
    


# In[21]:


def isBST2(root):
    if root==None:
        return 100000,-100000,True
    leftMin,leftMax,isLeftBST=isBST2(root.left)
    rightMin,rightMax,isRightBST=isBST2(root.right)
    
    minimum=min(leftMin,rightMin,root.data)
    maximum=max(leftMax,rightMax,root.data)
    isTreeBST=True
    if root.data<=leftMax or root.data>rightMin:
        isTreeBST=False
    if not(isLeftBST) or not(isRightBST):
        isTreeBST=False
        
    return minimum,maximum,isTreeBST


# In[26]:


root=takeTreeInputLevelWise()
printTreeDetailed(root)
nodeToRootPath(root,5)


# In[27]:


class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


# In[29]:


class BST:
    def __init__(self):
        self.root=None
        self.numNodes=0
    def printTreeHelper(self,root):
        if root==None:
            return
        print(root.data,end=":")
        if root.left!=None:
            print("L",root.left.data,end=",")
        if root.right!=None:
            print("R",root.right.data,end="")
        print()
        printTreeHelper(root.left)
        printTreeHelper(root.right)
        
    def printTree(self):
        printTreeHelper(self.root)
    def isPresentHelper(self,root,data):
        if root==None:
            return False
        if root.data==data:
            return True
        if root.data>data:
            #call on left
            return isPresentHelper(root.left,data)
        else:
            #Call on right
            return isPresentHelper(root.right,data)
    def isPresent(self,data):
        return isPresentHelper(self.root,data)
    def insert(self,data):
        return
    def deleteData(self):
        return False
    def count(self):
        return 0


# In[ ]:


b = BST()
b.insert(10)
b.insert(5)
b.insert(12)
print(b.isPresent(10))
print(b.isPresent(7))
print(b.deleteData(4))
print(b.deleteData(10))
print(b.count())


# In[ ]:




