from unittest import TestCase

from trees.binary_tree import Node, Tree


class TestNode(TestCase):

    def test_binary_search(self):
        self.root = Node(10)

        self.root.left = Node(5)
        self.root.left.left = Node(2)
        self.root.left.right = Node(6)

        self.root.right = Node(15)
        self.root.right.left = Node(13)
        self.root.right.right = Node(10000)

        self.tree = Tree(self.root)
        self.found = self.tree.root.binary_search(10000)
        self.assertEqual(self.found, True, ' the target was not found')
