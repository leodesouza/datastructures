class Node:
    def __init__(self, data, name):
        self.data = data
        self.name = name
        self.left = None
        self.right = None

    def binary_search(self, target):
        if self.data == target:
            return True

        if self.left and self.data > target:
            return self.left.binary_search(target)

        if self.right and self.data < target:
            return self.right.binary_search(target)
        return False


class Left(Node):
    def __init__(self, data):
        super().__init__(data, type(self).__name__)


class Right(Node):
    def __init__(self, data):
        super().__init__(data, type(self).__name__)


class Tree:
    def __init__(self, root):
        self.root = root
