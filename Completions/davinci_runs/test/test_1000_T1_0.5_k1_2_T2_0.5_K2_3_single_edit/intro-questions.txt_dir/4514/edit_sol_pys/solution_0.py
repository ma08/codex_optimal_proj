

import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree(preorder, inorder):
    if not preorder:
        return None
    root = Node(preorder[0])
    if len(preorder) == 1:
        return root
    root_inorder = inorder.index(preorder[0])
    root.left = build_tree(preorder[1:root_inorder+1], inorder[:root_inorder])
    root.right = build_tree(preorder[root_inorder+1:], inorder[root_inorder+1:])
    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=' ')
        inorder(root.right)


def preorder(root):
    if root:
        print(root.value, end=' ')
        preorder(root.left)
        preorder(root.right)


def main():
    preorder_list = [int(x) for x in sys.stdin.readline().split()]
    inorder_list = [int(x) for x in sys.stdin.readline().split()]
    root = build_tree(preorder_list, inorder_list)
    preorder(root)
    print()
    inorder(root)


if __name__ == "__main__":
    main()
