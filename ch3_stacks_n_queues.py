from random import randint
from leet.impl.LinkedList import LinkedList
from leet.impl.LinkedStack import LinkedStack
from leet.impl.LinkedQueue import LinkedQueue
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
