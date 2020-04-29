import queue
from Node import Node
class ComparableNode:
    def __init__(self, node):
        self.node = node

    def __gt__(self, other):
        x = self.node.cost + self.node.level
        y = other.node.cost + other.node.level
        return x > y

    def __repr__(self):
        return repr(self.node)
