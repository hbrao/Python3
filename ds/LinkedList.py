from ds.struct.LinkedNode import LinkedNode 
class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        """adds element at the start of the list O(1)"""
        self.head = LinkedNode(value, self.head)

    def append(self, value):
        """adds element at the end of the list O(n)"""
        n = LinkedNode(value)
        if self.head is None:
            self.head = n
            return self.head
        else:
            h = self.head
            while h.next is not None:
                h = h.next
            h.next = n
            return h

    def reverse(self):
        """Returns the reversed linked list"""
        r = LinkedList()
        for value in self:
            r.prepend(value)
        return r

    def __iter__(self):
        """Iterator of values in the list"""
        n = self.head
        while n is not None:
            yield n.value
            n = n.next

    def __repr__(self):
        """String representation of the list"""
        if self.head is None:
            return 'lnk:[]'
        return "lnk:[{0:s}]".format('->'.join(map(str, self)))
