from leet.core.TreeNode import TreeNode


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, val):
        self.root = self.add_to_subtree(self.root, val)

    def add_to_subtree(self, parent, val):
        if parent is None:
            return TreeNode(val)
        else:
            if val > parent.val:
                parent.right = self.add_to_subtree(parent.right, val)
            else:
                parent.left = self.add_to_subtree(parent.left, val)
            return parent

    def add_all(self, data):
        for val in data:
            self.add(val)

    def __repr__(self):
        if self.root is None:
            return "[]"
        else:
            return "inorder:" + ",".join(self.root.inorder())
