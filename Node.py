class Node :
    def __init__(self,matrix,x,y,newX,newY,level,parent):
        self.parent=parent
        self.matrix=matrix
        self.cost=100000000000000
        self.level=level
        self.newX=newX
        self.newY=newY

        #self.matrix[x][y]=self.matrix[x][y]+self.matrix[newX][newY]
        #self.matrix[newX][newY]=self.matrix[x][y]-self.matrix[newX][newY]
        #self.matrix[x][y]=self.matrix[x][y]-self.matrix[newX][newY]

mat = [[0 for i in range(3)] for j in range(3)]