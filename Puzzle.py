import queue
import  heapq
from Node import Node,ComparableNode
#from collections import defaultdict
class Puzzle:
    def __init__(self):
        #self.count=0
        self.rowmap={}
        self.colmap={}
        self.dimension=4
        self.row=[1,0,-1,0]
        self.col=[0,-1,0,1]
    def calculateCost(self,initial, goal):
        count = 0
        for i in range(len(initial)):
            for j in range(len(initial)):
                if (initial[i][j] != 0 and initial[i][j] != goal[i][j]):
                    count = count + 1
        return count


    def Shifting(self,matrix):
       for i in range(len(matrix)):
            for j in range(len(matrix)):
                m = matrix[i][j]
                self.rowmap[m] = i
                self.colmap[m] = j

       """for key, value in self.rowmap.items():
            print('elemnt:{},Rownumber {}'.format(key, value))
       print()
       for key, value in self.colmap.items():
            print('elemnt:{},Columnnumber {}'.format(key, value))
       print()
       """
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
        #print(type(cst))
        return cst
    def printMatrix(self,matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                print(matrix[i][j], end=" ")
            print()
    def isSafe(self,x,y):
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
        for i in range(0,len(matrix1),1):
            for j in range(0,len(matrix2),1):
                if(matrix1[i][j]!=matrix2[i][j]):
                    count=count+1
        print("Minimumnumber of Swap Required : {}".format(count))

    def solveManhatton(self,initial,goal,x,y):
        root=Node(initial,x,y,x,y,0,None)
        root.cost=self.Manhatton(initial,goal)
        pq=queue.PriorityQueue()
        #pq.put(ComparableNode(root))
        pq.put(ComparableNode(root.cost,root.level,root.matrix,x,y,x,y,None))
        #print(root.x)
        #min=pq.get()
        #print(min)
        #min=pq.get()
        #print(min.papa)
        #print(min.cost)
        #self.printMatrix(min.matrix)
        #self.printPath(min)

            #self.printMatrix(min.matrix)
        while(not pq.empty()):
            min=pq.get()
            node1 = Node(min.matrix, min.x, min.y, min.x, min.y, min.level, min.parent)
            if(min.cost==0):

                #node1 = Node(min.matrix, min.x, min.y, min.x,min.y,min.level, min.parent)
                self.printPath(min)
                #self.printMatrix(min.matrix)
                #self.printMatrix(min.matrix)
                #print(min.matrix)
                return
           # node = Node(min.matrix, min.x, min.y, min.x, min.y, min.level, min.parent)
            for i in range(4):

                if(self.isSafe((node1.x+self.row[i]),(node1.y+self.col[i]))):
                    #node=Node(min.matrix,min.x,min.y,min.x,min.y,min.level,min.parent)
                    #child=Node(min.matrix, min.x, min.y, min.x + self.row[i], min.y + self.col[i], min.level + 1, min)
                    child=Node(node1.matrix,node1.x,node1.y,node1.x+self.row[i],node1.y+self.col[i],node1.level+1,node1)
                    child.cost=self.calculateCost(child.matrix,goal)
                    pq.put(ComparableNode(child.cost,child.level,child.matrix,child.x, child.y,child.x,child.y,node1))















matrix4=[[2 ,3, 4, 0], [1 ,5, 7, 8] ,[9, 6 ,10, 12], [13, 14, 11, 15]] #thikthak
matrix1=[[1, 2, 6, 3], [4, 9, 5, 7], [8, 13, 11, 15], [12, 14, 0, 10]]
matrix2=[[5, 1 ,7 ,3], [9 ,2 ,11 ,4], [13 ,6 ,15 ,8], [0 ,10 ,14 ,12]]#thiktha
matrix3=[[1, 2 ,3, 4] ,[5, 6, 7, 8], [9, 10, 11, 12],[ 13, 15, 14, 0]]
goal=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
x=3
y=2
p=Puzzle()

if(p.isSolvable(matrix1)):
        p.SwapNumber(matrix1,goal)
        p.Shifting(matrix1)
        p.Manhatton(matrix1,goal)
        p.solveManhatton(matrix1,goal,x,y)
#print(p.calculateCost(matrix2,goal))
#p.Shifting(matrix2)
#print(p.Manhatton(matrix2,goal))
#goal=Node(matrix,0,0,0,0,0,None)
#n=Node(matrix,0,0,0,0,0,goal)
#p.printPath(n)
#p.solveManhatton(matrix2,goal,0,0)
#p.Manhatton(matrix,goal)
#p.printMatrix(matrix)
#p.isSolvable(matrix)


