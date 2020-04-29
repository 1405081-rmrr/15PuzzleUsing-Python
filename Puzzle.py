import queue
import  heapq
from Node import Node
from PQ import ComparableNode
from collections import defaultdict
class Puzzle:
    def __init__(self):
        self.count=0
        self.rowmap={}
        self.colmap={}
        self.dimension=4
    def calculateCost(self,initial, goal):
        #self.count=count = 0
        for i in range(len(initial)):
            for j in range(len(initial)):
                if (initial[i][j] != 0 and initial[i][j] != goal[i][j]):
                    self.count = self.count + 1
        return self.count

    def Shifting(self,matrix):
       for i in range(len(matrix)):
            for j in range(len(matrix)):
                m = matrix[i][j]
                self.rowmap[m] = i
                self.colmap[m] = j

       for key, value in self.rowmap.items():
            print('elemnt:{},Rownumber {}'.format(key, value))
       print()
       for key, value in self.colmap.items():
            print('elemnt:{},Columnnumber {}'.format(key, value))
       print()
    def Count(self,a,i,j):
        p=self.rowmap.get(a)
        q=self.colmap.get(a)
        cost1=abs(p-i)
        cost2=abs(q-j)
        cost=cost1+cost2
        return cost
    def Manhatton(self,initial,goal):
        cst=0
        v=0
        for i in range(len(initial)):
            for j in range (len(initial)):
                if(goal[i][j]!=0 and initial[i][j]!=goal[i][j]):
                    v=goal[i][j]
                    cnt=self.Count(v,i,j)
                    cst =cst + cnt
        print(type(cst))
        return cst
    def printMatrix(self,matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                print(matrix[i][j], end=" ")
            print()
    def isSafe(x,y):
        return (x>=0 and x<self.dimension and y>=0 and y<self.dimension)
    def printPath(self,root):
        if(root==None):
            return
        self.printPath(root.parent)
        self.printMatrix(root.matrix)
        print()
    def isSolvable(self,matrix):
        count=0
        p=0
        array=[]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                m=matrix[i][j]
                array.append(m)
        anotherArray=[]
        anotherArray=array.copy()
        for i in range(len(anotherArray)-1):
            for j in range((i+1),len(anotherArray),1):
                if(anotherArray[i]!=0 and anotherArray[j]!=0 and anotherArray[i]>anotherArray[j]):
                    count=count+1
        x=self.position(anotherArray)
        print("Number of inversions :  {}".format(count))
        if(x==True):
            print("X is in the 2nd or 4th row")
        elif(x==False):
            print("X is in the 1st or 3rd row")
        if((count%2==0 and x==True ) or (count%2==1 and x==False)):
            print("It is Solvable")
        else:
            print("It is NOT Solvable")
        return ((count%2==0 and x==True ) or (count%2==1 and x==False))
    def position(self,array):
        b=0
        for i in range(4,8,1):
            if(array[i]!=0):
                continue
            elif(array[i]==0):
                b=1
        for i in range(12,len(array),1):
            if(array[i]!=0):
                continue
            elif(array[i]==0):
                b=1
        return b%2==1
    def SwapNumber(self,matrix1,matrix2):
        count=0
        for i in range(0,len(matrix),1):
            for j in range(0,len(matrix2),1):
                if(matrix1[i][j]!=matrix2[i][j]):
                    count=count+1
        print("Minimumnumber of Swap Required : {}".format(count))

    def solveManhatton(self,initial,goal,x,y):
        root=Node(initial,x,y,x,y,0,None)
        root.cost=self.Manhatton(initial,goal)
        print(root.cost)
        pq=queue.PriorityQueue()
        pq.put(ComparableNode(root))





matrix=[[13,1,2,4],[5,0,3,7],[9,6,10,12],[15,8,11,14]]
matrix2=[[3, 9, 1, 15], [14 ,11, 4, 6], [13, 0, 10, 12],[ 2, 7, 8, 5]]
matrix3=[[2 ,6 ,5 ,4 ],[1 ,0 ,3, 8] ,[9 ,10 ,7 ,11], [13 ,14 ,15 ,12]]
goal=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
p=Puzzle()
print(p.calculateCost(matrix3,goal))
p.Shifting(matrix3)
print(p.Manhatton(matrix3,goal))
#goal=Node(matrix,0,0,0,0,0,None)
#n=Node(matrix,0,0,0,0,0,goal)
#p.printPath(n)
p.solveManhatton(matrix3,goal,0,0)
#p.Manhatton(matrix,goal)
#p.printMatrix(matrix)
#p.isSolvable(matrix)


