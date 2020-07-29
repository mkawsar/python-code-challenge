import unittest
from problem3_revised import findLCA, Node


class TestProblem3(unittest.TestCase):

    def test_lca(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        root.left.left.left = Node(8)
        root.left.left.right = Node(9)

        self.assertEqual(findLCA(root, 8, 5), 2)
        self.assertEqual(findLCA(root, 7, 6), 3)
        self.assertEqual(findLCA(root, 3, 7), 3)
        self.assertEqual(findLCA(root, 6, 7), 3)
        self.assertEqual(findLCA(root, 6, 6), 6)
        self.assertEqual(findLCA(root, 8, 3), 1)
        self.assertEqual(findLCA(root, 8, 4), 4)
        self.assertEqual(findLCA(root, 8, 9), 4)


if __name__ == '__main__':
    unittest.main()
