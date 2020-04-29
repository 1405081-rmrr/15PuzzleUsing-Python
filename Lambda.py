"""import heapq
import queue
portfolio = [
       {'name': 'IBM', 'shares': 200, 'price': 108.68},
       {'name': 'AAPL', 'shares': 75, 'price': 277.97},
       {'name': 'FB', 'shares': 40, 'price': 170.28},
       {'name': 'HPQ', 'shares':125, 'price': 17.18},
       {'name': 'UBER', 'shares': 50, 'price': 22.60},
       {'name': 'TWTR', 'shares': 95, 'price': 29.29}
]
cheap_stocks = heapq.nsmallest(3, portfolio, key=lambda s: (s['price']+s['shares']))
expensive_stocks = heapq.nlargest(3, portfolio, key=lambda s: (s['price']+s['shares']))
print("Cheap Stocks: ", cheap_stocks)
print("Expensive Stocks: ", expensive_stocks)


import queue
q= queue.PriorityQueue()
q.put(portfolio,key=lambda s:(s['price']))
for i in range(q.qsize()):
       print(q.get(i))
"""
#@functools.total_ordering
import queue
class Node:
    def __init__(self, val,cost,matrix):
        self.val = val
        self.cost=cost
        self.matrix=matrix

    #def __repr__(self):
    def __str__(self):
        return "Node(val={} cost={})".format(self.val,self.cost)

matrix=matrix=[[13,1,2,4],[5,0,3,7],[9,6,10,12],[15,8,11,14]]
a = Node(10,5,matrix) #15
b = Node(40,65,matrix) #105
c = Node(4,300,matrix) #304

class ComparableNode:
    def __init__(self, node):
        self.node = node

    def __gt__(self, other):
       x=self.node.cost+self.node.val
       y=other.node.cost+other.node.val
       return x>y

    """def __eq__(self, other):
        return self.node.val == other.node.val
        
       """
    def __str__(self):
      return repr(self.node)


p = queue.PriorityQueue()
p.put(ComparableNode(a))
p.put(ComparableNode(b))
p.put(ComparableNode(c))
for i in range(p.qsize()):
       print(type(p.get(i)))
       break


