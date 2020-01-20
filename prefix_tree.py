WORD_KEY = '\n'


class PrefixTree:
    def __init__(self):
        self.head = {}

    def add(self, word):
        if len(word) == 0:
            return False

        d = self.head;
        for c in word:
            if c not in d:
                d[c] = {}

            d = d[c]

        d[WORD_KEY] = True

    def __contains__(self, word):
        d = self.head
        for c in word:
            if c not in d:
                return False
            else:
                d = d[c]

        if WORD_KEY in d:
            return True
        else:
            return False


d = PrefixTree()
d.add('inch')
d.add('in')

print('in' in d)
print('inc' in d)
print('inch' in d)
