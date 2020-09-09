from ds.struct.LinkedNode import LinkedNode
class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, value):
        """Add element at the tail end of list O(1)"""
        n = LinkedNode(value)
        if self.is_empty():
            self.head = self.tail = n
        else:
            self.tail.next = n
            self.tail = n

    def deque(self):
        """Remove element from front end of the list O(1)"""
        if not self.is_empty():
            n = self.head.value
            self.head = self.head.next
            return n
        else:
            raise Exception("Queue is empty !")

    def __iter__(self):
        if not self.is_empty():
            n = self.head
            while n is not None:
                yield n.value
                n = n.next

    def __repr__(self):
        if self.is_empty():
            return "que:[]"
        else:
            return "que:[{0:s}]".format('->'.join(map(str, self)))