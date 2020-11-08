from pyds.classes.LinkedQueue import LinkedQueue
from pyds.classes.BinaryTree import  BinaryTree
from pyds.classes.DirectedGraphAL import DirectedGraphAL
from pyds.core.TreeNode import TreeNode
from random import randint


def s1_has_path_between_nodes(g: DirectedGraphAL, s: int, t: int) -> str:
    visited = [0] * g.size
    q = LinkedQueue()
    q.enqueue(s)
    while not q.is_empty():
        v = q.deque()
        visited[v] = 1
        for e in g.vertices[v]:
            if e[0] == t:
                return True
            else:
                if visited[e[0]] == 0:
                    q.enqueue(e[0])
    return False


def s2_helper(bt, arr, s, e):
    if s == e:
        print("Adding {}".format(arr[s]))
        bt.add(arr[s])
    elif e - s == 1:
        print("Adding {}".format(arr[s]))
        bt.add(arr[s])
        print("Adding {}".format(arr[e]))
        bt.add(arr[e])
    elif e - s > 1:
        mid = (s + e) // 2
        print("Adding {}".format(arr[mid]))
        bt.add(arr[mid])
        s2_helper(bt, arr, s, mid - 1)
        s2_helper(bt, arr, mid + 1, e)


def s2_build_tree_sorted_array(arr) -> BinaryTree:
    bt = BinaryTree()
    s2_helper(bt, arr, 0, len(arr) - 1)
    return bt


def s3_bfs_tree(bn: TreeNode, depth, res):
    if bn is not None:
        if depth >= len(res):
            res.append([])
        res[depth].append(bn.value)
        s3_bfs_tree(bn.left, depth + 1, res)
        s3_bfs_tree(bn.right, depth + 1, res)


def s3_collect_nodes(bt: BinaryTree) -> []:
    res = []
    s3_bfs_tree(bt.root, 0, res)
    return res


grh1 = DirectedGraphAL(5)
grh1.add_edge(0, 1, 1)
grh1.add_edge(2, 3, 1)
grh1.add_edge(1, 3, 1)
grh1.add_edge(3, 4, 1)
grh1.add_edge(4, 1, 1)

print(s1_has_path_between_nodes(grh1, 0, 2))

arr1 = sorted([randint(10, 99) for i in range(10)])
print(arr1)
btr1 = s2_build_tree_sorted_array(arr1)

print(s3_collect_nodes(btr1))

btr2 = BinaryTree()
btr2.add(30)
btr2.add(15)
btr2.add(45)
btr2.add(10)
btr2.add(25)
btr2.add(35)
btr2.add(55)
btr2.add(31)
btr2.add(38)

btr3 = BinaryTree()
btr3.add(30)
btr3.add(15)
btr3.add(45)
btr3.add(10)
btr3.add(25)
btr3.add(35)
btr3.add(55)
btr3.add(31)
btr3.add(38)
btr3.add(36)

