class Stack:
    def __init__(self):
        self.data = []

    def push(self, val):
        self.data.append(val)

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop()


class MonotonicStack:
    def __init__(self, data):
        self.data = data
        self.mono = []
