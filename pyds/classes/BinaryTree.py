from pyds.core.TreeNode import TreeNode
class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self.root = self.root.add(val)

    def addAll(self, data) :
        for val in data:
            self.add(val)

    def __repr__(self):
        if self.root is None :
            return "EMPTY"
        else:
            return self.root.inorder()