#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Rat In a Maze

def printPathHelper(x,y,maze,n,solution):
    if x==n-1 and y==n-1:
        solution[x][y]=1
        print(solution)
        return
    if x<0 or y<0 or x>=n or y>=n or maze[x][y]==0 or solution[x][y]==1:
        return
    
    solution[x][y]=1
    printPathHelper(x+1,y,maze,n,solution)
    printPathHelper(x,y+1,maze,n,solution)
    printPathHelper(x,y-1,maze,n,solution)
    printPathHelper(x-1,y,maze,n,solution)
    solution[x][y]=0
    return
    
def printPath(maze):
    n = len(maze)
    solution = [[0 for j in range(n)] for i in range(n)]
    printPathHelper(0,0,maze,n,solution)
    

n = int(input())
maze = []
for i in range(n):
    row = [int(ele) for ele in input().split()]
    maze.append(row)
    
    
printPath(maze)


# In[ ]:


def isSafe(row,col,board,n):
    #vertical direction
    i=row-1
    while i>=0:
        if board[i][col]==1:
            return False
        i-=1
    i=row-1
    j=col-1
    
    while i>=0 and j>=0:
        if board[i][j]==1:
            return False
        i-=1
        j-=1
    i=row-1
    j=col+1
    while i>=0 and j<n:
        if board[i][j]==1:
            return False
        i-=1
        j+=1
    
    return True
def printPathsHelper(row,n,board):
    if row==n:
        for i in range(n):
            for j in range(n):
                print(board[i][j],end=' ')
        print()
        return
    for col in range(n):
        if isSafe(row,col,board,n) is True:
            board[row][col]=1
            printPathsHelper(row+1,n,board)
            board[row][col]=0
    return
def printPaths(n):
    board=[[0 for j in range(n)]for i in range(n)]
    printPathsHelper(0,n,board)
n=int(input())
printPaths(n)


# In[ ]:




