BUCKET_SIZE = 10
BUCKET_COUNT = 3
THRESHOLD = .5


class Stack:
    def __init__(self):
        self.stk = [None] * BUCKET_COUNT
        for i in range(BUCKET_COUNT):
            self.stk[i] = [None] * BUCKET_SIZE
        self.tail = -1

    def extract_bucket_and_top(self):
        bkt = self.tail // int(BUCKET_SIZE * THRESHOLD)
        top = self.tail % int(BUCKET_SIZE * THRESHOLD)
        return bkt, top

    def is_empty(self) -> bool:
        return self.tail == -1

    def is_full(self) -> bool:
        return self.tail == BUCKET_COUNT * int(BUCKET_SIZE * THRESHOLD) - 1

    def push(self, value):
        """Adds element at the end of the list O(1)"""
        if not self.is_full():
            self.tail += 1
            bkt, top = self.extract_bucket_and_top()
            self.stk[bkt][top] = value
        else:
            raise Exception("Stack is Full ! {}".format(self.extract_bucket_and_top()))

    def pop(self):
        """Removes element from the end of the list O(1)"""
        bkt, top = self.extract_bucket_and_top()
        data = self.stk[bkt][top]
        self.tail += -1
        return data

    def __iter__(self):
        bkt, top = self.extract_bucket_and_top()
        while bkt >= 0:
            for i in range(top, -1, -1):
                yield self.stk[bkt][i]
            bkt += -1
            top = (int(BUCKET_SIZE * THRESHOLD) - 1)

    def __repr__(self):
        """Shows the stack from top to bottom"""
        return "stk:[{0:s}]".format('->'.join(map(str, self)))


class LinkedNode:
    def __init__(self, value=None, tail=None):
        """Node in a linked list"""
        self.value = value
        self.next = tail


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
            v = self.head.value
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


class DirectedGraphAL:
    def __init__(self, size):
        self.vertices = [None] * size
        self.size = size

    def add_edge(self, u, v, w=1):
        """Adds an edge (u,v) with weight w"""
        # Create an adjacency list to store all edges emanating from vertex u
        if self.vertices[u] is None:
            self.vertices[u] = []
        # Edge information is stored as tuple and can't be updated.
        # Hence, remove if an edge is already existing.
        for e in self.vertices[u]:
            if e[0] == v:
                print("Removing an existing edge {} from {}".format(e, u))
                self.vertices[u].remove(e)
                break
        # Add edge info with weight.
        self.vertices[u].append((v, w))

    def neighbors(self, u):
        if self.vertices[u]:
            for e in self.vertices[u]:
                yield e

    def __repr__(self):
        rep = 'grh:['
        for v in range(self.size):
            for e in self.neighbors(v):
                rep += str(v) + '->' + str(e) + ', '
        rep += ']'
        return rep


class BinaryNode:
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
            return BinaryNode(val)
        parent.add(val)
        # Return the parent as it is.
        # This ensures left / right nodes of grand parent nodes untouched.
        return parent


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, val):
        if self.root is None:
            self.root = BinaryNode(val)
        else:
            self.root = self.root.add(val)
