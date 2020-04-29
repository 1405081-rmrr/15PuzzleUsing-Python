class Node:
    def __init__(self,x,node):
        self.x=x
        self.node=node
    def print_node(self):
        temp=self
        while temp!=None:
            print(temp.x)
            temp=temp.node


l=Node(10,None)
m=Node(12,l)
p=Node(14,m)
l.print_node()
m.print_node()
p.print_node()