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