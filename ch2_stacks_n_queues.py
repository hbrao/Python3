from ds import LinkedStack, LinkedList, LinkedQueue
from random import randint

l = LinkedList()
s = LinkedStack()
q = LinkedQueue()
for i in range(12):
    v = randint(10, 99)
    l.append(v)
    s.push(v)
    q.enqueue(v)

print(l)
print(s)
print(q)
