class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0

    def add(self, val):
        if val > self.value:
            self.right = self.add_to_subtree(self.right, val)
        else:
            self.left = self.add_to_subtree(self.left, val)
        return self

    def add_to_subtree(self, parent, val):
        if parent is None:
            return TreeNode(val)
        parent.add(val)
        # Return the parent as it is.
        # This ensures left / right nodes of grand parent nodes untouched.
        return parent
