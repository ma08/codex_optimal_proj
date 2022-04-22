import sys
sys.setrecursionlimit(10**6)


class Node:
    def __init__(self, _id, left_id, right_id):
        self.id = _id
        self.left_id = left_id
        self.right_id = right_id

n = int(sys.stdin.readline())
tree = [Node(0, 0, 0)]
for i in range(n):
    id, left_id, right_id = map(int, sys.stdin.readline().split())
    tree.append(Node(id, left_id, right_id))

def preorder(node):
    print(' ' + str(node.id), end='')
    if node.left_id != -1:
        preorder(tree[node.left_id])
    if node.right_id != -1:
        preorder(tree[node.right_id])

def inorder(node):
    if node.left_id != -1:
        inorder(tree[node.left_id])
    print(' ' + str(node.id), end='')
    if node.right_id != -1:
        inorder(tree[node.right_id])

def postorder(node):
    if node.left_id != -1:
        postorder(tree[node.left_id])
    if node.right_id != -1:
        postorder(tree[node.right_id])
    print(' ' + str(node.id), end='')

print('Preorder')
preorder(tree[1])
print()
print('Inorder')
inorder(tree[1])
print()
print('Postorder')
postorder(tree[1])
print()
