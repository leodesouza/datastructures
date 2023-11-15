from unittest import TestCase

from trees.binary_tree import Node, Tree, Left, Right


class TestNode(TestCase):

    def setUp(self):
        self.root = Node(10, 'root')

        self.root.left = Left(5)
        self.root.left.left = Left(2)
        self.root.left.right = Right(6)

        self.root.right = Right(15)
        self.root.right.left = Left(13)
        self.root.right.right = Right(10000)

        self.tree = Tree(self.root)

    def test_binary_search_10000_returns_true(self):
        self.found = self.tree.root.binary_search(10000)
        self.assertEqual(self.found, True)

    def test_binary_search_5_returns_false(self):
        self.found = self.tree.root.binary_search(7)
        self.assertEqual(self.found, False, ' the target was not found')
