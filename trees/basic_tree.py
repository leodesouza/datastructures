class Node:
    def __init__(self, data):
        self.data = data
        self.left = Node
        self.right = Node


node = Node(10)

node.left = Node(5)
node.right = Node(15)

node.left.left = Node(2)
node.left.right = Node(6)

node.right.left = Node(13)
node.right.right = Node(10000)

print(node.right.data)
print(node.right.right.data)
