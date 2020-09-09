from ds.struct.BinaryNode import BinaryNode
class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, val):
        if self.root is None:
            self.root = BinaryNode(val)
        else:
            self.root = self.root.add(val)