#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''Problem Statement
You are given a 'N' * 'N' maze with a rat placed at 'MAZE[0][0]'. Find and print all paths that rat can follow to reach its destination i.e. 'MAZE['N' - 1]['N' - 1]'. Rat can move in any direc­tion ( left, right, up and down).
Value of every cell in the 'MAZE' can either be 0 or 1. Cells with value 0 are blocked means the rat can­not enter into those cells and those with value 1 are open.'''


# In[ ]:


def printPathHelper(x,y,maze,n,solution):
    if x==n-1 and y==n-1:
        solution[x][y]=1
        print(solution)
        return
    
    if x<0 or y<0 or x>=n or y>=n or maze[x][y]==0 or solution[x][y]==1:
        return
    
    solution[x][y]==1
    printPathHelper(x+1,y,maze,n,solution)
    printPathHelper(x,y+1,maze,n,solution)
    printPathHelper(x-1,y,maze,n,solution)
    printPathHelper(x,y-1,maze,n,solution)
    solution[x][y]=0
    return
def printPath(maze):
    n=len(maze)
    solution=[[0 for j in range(n)] for i in range(n)]
    printPathHelper(0,0,maze,n,solution)
    
n=int(input())
maze=[]
for i in range(n):
    row=[int(ele) for ele in input().split()]
    maze.append(row)
    
printPath(maze)


# In[ ]:


'''Problem Statement
You are given an integer 'N'. For a given 'N' x 'N' chessboard, find a way to place 'N' queens such that no queen can attack any other queen on the chessboard.
A queen can be killed when it lies in the same row, or same column, or the same diagonal of any of the other queens. You have to print all such configurations.'''


# In[2]:


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




