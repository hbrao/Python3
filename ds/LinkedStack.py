from ds.struct.LinkedNode import LinkedNode  
class LinkedStack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, value):
        """Add element at the front end of list O(1)"""
        self.head = LinkedNode(value, self.head)

    def pop(self):
        """Remove element from front end of the list O(1)"""
        if not self.is_empty():
            print('Removing ' + str(self.head.value))
            self.head = self.head.next

    def __iter__(self):
        if not self.is_empty():
            n = self.head
            while n is not None:
                yield n.value
                n = n.next

    def __repr__(self):
        if self.is_empty():
            return "stk:[]"
        else:
            return "stk:[{0:s}]".format('->'.join(map(str, self)))