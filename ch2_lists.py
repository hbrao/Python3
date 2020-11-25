from random import randint
from leet.core.ListNode import ListNode
from leet.impl.LinkedList import LinkedList


def s1_remove_duplicates(l: LinkedList) -> None:
    n1 = l.head
    while n1 is not None:
        val = n1.val
        prev = n1
        n2 = n1.next
        while n2 is not None:
            if n2.val == val:
                prev.next = n2.next
            else:
                prev = n2
            n2 = n2.next
        n1 = n1.next


def s2_kth_to_last(l: LinkedList, i: int) -> int:
    nk = l.head
    n2 = l.head
    for tmp in range(i):
        if n2 is not None:
            n2 = n2.next
        else:
            raise ValueError("Not enough size to find {} element".format(i))
    while nk is not None and n2 is not None:
        nk = nk.next
        n2 = n2.next
    return nk.val


def s3_del_node(node: ListNode) -> None:
    prev = None
    while node.next is not None:
        node.val = node.next.val
        prev = node
        node = node.next
    prev.next = None


def s4_list_partition(l: LinkedList, x: int) -> None:
    if l.head is None or l.head.next is None:
        return

    prev = l.head
    n = l.head.next
    while n is not None:
        if n.val < x:
            prev.next = n.next
            l.prepend(n.val)
        else:
            prev = n
        n = n.next


def s5_sum_lists(l1: LinkedList, l2: LinkedList) -> LinkedList:
    s = LinkedList()
    n1 = l1.head
    n2 = l2.head
    q = 0
    r = 0
    while n1 or n2:
        x = y = 0
        if n1:
            x = n1.val
            n1 = n1.next
        if n2:
            y = n2.val
            n2 = n2.next
        r = (x + y + q) % 10
        q = (x + y + q) // 10
        s.prepend(r)
    if q != 0:
        s.prepend(q)
    return s


def s6_is_palindrome(l: LinkedList) -> bool:
    r = l.reverse()
    n1 = l.head
    n2 = r.head
    while n1 is not None:
        if n1.val != n2.val:
            return False
        n1 = n1.next
        n2 = n2.next
    return True


def s7_get_intersection(l1: ListNode, l2: ListNode) -> ListNode:
    n1 = l1
    n2 = l2
    l1s = l2s = 1
    insect = None
    while n1.next is not None or n2.next is not None:
        if n1.next:
            n1 = n1.next
            l1s += 1
        if n2.next:
            n2 = n2.next
            l2s += 1
        if insect is None and n1 is n2:
            insect = n1
    if insect and l1s == l2s:
        return insect
    elif insect:
        j = abs(l1s - l2s)
        if l1s > l2s:
            n1 = l1
            n2 = l2
        else:
            n1 = l2
            n2 = l1
        for tmp in range(j):
            n1 = n1.next
        return s7_get_intersection(n1, n2)
    else:
        return None


def s8_detect_loop(l: LinkedList) -> ListNode:
    n1 = l.head
    n2 = l.head
    while n1 and n2 and n2.next:
        n1 = n1.next
        n2 = n2.next.next
        if n1 is n2:
            n1 = l.head
            while n1 and n2:
                if n1 is n2:
                    return n1
                n1 = n1.next
                n2 = n2.next


lst1 = LinkedList()
lst2 = LinkedList()
for temp in range(20):
    lst1.prepend(randint(1, 10))
for temp in range(10):
    lst2.prepend(randint(1, 10))

print(lst1)
s1_remove_duplicates(lst1)
print(lst1)

k = 5
print("{}'th to the last is {}".format(k, s2_kth_to_last(lst1, k)))

inode = lst1.head
inode_num = 3
print("Deleting {}'th internal node".format(inode_num))
while inode_num > 1 and inode is not None:
    inode = inode.next
    inode_num -= 1
s3_del_node(inode)
print(lst1)

print("Re-order list around value {}".format(lst1.head.val))
s4_list_partition(lst1, lst1.head.val)
print(lst1)

print("Sum of lists \n {} \n {} \n {}".format(lst1, lst2, s5_sum_lists(lst1, lst2)))

str1 = "abcba"
lst3 = LinkedList()
for c in str1:
    lst3.append(c)
print("{} is palindrome ? Ans : {}".format(lst3, s6_is_palindrome(lst3)))

lst1 = LinkedList()
lst2 = LinkedList()
l1size = 10
l2size = 10
for temp in range(l1size):
    lst1.prepend(randint(10, 99))
for temp in range(l2size):
    lst2.prepend(randint(10, 99))
print(lst1)
print(lst2)

l1_j = randint(1, l1size // 2)
l2_k = randint(1, l2size // 2)
nd1 = lst1.head
for i in range(l1_j - 1):
    nd1 = nd1.next
nd2 = lst2.head
for i in range(l2_k - 1):
    nd2 = nd2.next
print("Creating intersection: {} + {} ".format(l1_j, l2_k))
nd2.next = nd1
print(lst1)
print(lst2)
print(s7_get_intersection(lst1.head, lst2.head).val)

print(lst1)
nd1 = None
nd2 = lst1.head
i = randint(l1size // 3, l1size // 2)
counter = 1
while nd2.next is not None:
    if counter == i:
        nd1 = nd2
    nd2 = nd2.next
    counter += 1
print("Last node is {} loop start is {}".format(nd2.val, nd1.value))
nd2.next = nd1
print("Detected a loop at node {}".format(s8_detect_loop(lst1).val))
