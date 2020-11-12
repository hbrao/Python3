class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def inorder(self):
        if self.left is not None:
            for key in self.left.inorder():
                yield str(key)
        yield str(self.val)
        if self.right is not None:
            for key in self.right.inorder():
                yield str(key)
