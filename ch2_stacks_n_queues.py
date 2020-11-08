from random import randint
from pyds.classes.LinkedList import LinkedList
from pyds.classes.LinkedStack import LinkedStack
from pyds.classes.LinkedQueue import LinkedQueue
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
