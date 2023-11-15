class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def binary_search(self, target):
        if self.data == target:
            True

        if self.left and self.data > target:
            return self.left.binary_search(target)

        if self.right and self.data < target:
            return self.right.binary_search(target)


class Tree:
    def __init__(self, root):
        self.root = root
