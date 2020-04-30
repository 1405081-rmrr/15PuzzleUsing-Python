class Node :
    cost=100000000000000
    def __init__(self,matrix,x,y,newX,newY,level,parent):
        self.parent=parent
        self.matrix=matrix
        self.level=level
    #def __repr__(self):
        #return "Node(Level={} cost={})".format(self.level,self.cost)
        for i in range(4):
            for j in range(4):
                self.matrix[i][j]=matrix[i][j]
        self.matrix[x][y]=self.matrix[x][y]+self.matrix[newX][newY]
        self.matrix[newX][newY]=self.matrix[x][y]-self.matrix[newX][newY]
        self.matrix[x][y]=self.matrix[x][y]-self.matrix[newX][newY]
        self.x=newX
        self.y=newY

class ComparableNode:
    def __init__(self, cost,level,matrix,x,y,x1,y1,parent):
            self.cost=cost
            self.level=level
            self.matrix=matrix
            self.x=x1
            self.y=y1
            self.parent=parent

            #self.matrix[x][y] = self.matrix[x][y] + self.matrix[x1][y1]
            #self.matrix[x1][y1] = self.matrix[x][y] - self.matrix[x1][y1]
            #self.matrix[x][y] = self.matrix[x][y] - self.matrix[x1][y1]


    def __gt__(self, other):
        # x = self.node.cost + self.node.level
        # y = other.node.cost + other.node.level
        # return x > y
        p=self.cost+self.level
        q=other.level+other.cost
        return p>q


    #def __repr__(self):
        #return repr(self.matrix)
         #return self.matrix
