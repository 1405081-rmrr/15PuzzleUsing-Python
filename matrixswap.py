class Node :
    def __init__(self,matrix,x,y,newX,newY,level,parent):
        self.parent=parent
        self.matrix=matrix
        self.cost=10**100
        self.level=level
        self.newX=newX
        self.newY=newY

        self.matrix[x][y]=self.matrix[x][y]+self.matrix[newX][newY]
        self.matrix[newX][newY]=self.matrix[x][y]-self.matrix[newX][newY]
        self.matrix[x][y]=self.matrix[x][y]-self.matrix[newX][newY]

    @staticmethod
    def swap(matrix2,matrix3):
        for i in range(3):
            for j in range(3):
                matrix2[i][j] = matrix2[i][j] + matrix3[i][j]
                matrix3[i][j] = matrix2[i][j] - matrix3[i][j]
                matrix2[i][j] = matrix2[i][j] - matrix3[i][j]
        print("Matrix 1 is : ")
        for i in range(3):
            for j in range(3):
                print(matrix2[i][j],end=" ")
            print()
        print("Matrix 2 is : ")
        for i in range(3):
            for j in range(3):
                print(matrix3[i][j], end=" ")
            print()

mat=[[0 for i in range(3)] for j in range(3)]
p=Node(mat,0,0,0,0,0,None)
matrix1=[[1 for i in range(3)] for j in range(3)]
matrix2=[[2 for i in range(3)] for j in range(3)]
p.swap(matrix1,matrix2)

"""from Node import Node
mat=[[0 for i in range(3)] for j in range(3)]
p=Node(mat,0,0,0,0,0,None)
matrix1=[[1 for i in range(3)] for j in range(3)]
matrix2=[[2 for i in range(3)] for j in range(3)]
p.swap(matrix1,matrix2)
"""
