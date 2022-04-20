

import sys

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(val, self.root)

    def _insert(self, val, node):
        if val < node.val:
            if node.left is not None:
                self._insert(val, node.left)
            else:
                node.left = Node(val)
        else:
            if node.right is not None:
                self._insert(val, node.right)
            else:
                node.right = Node(val)

    def find(self, val):
        if self.root is None:
            return False
        else:
            return self._find(val, self.root)

    def _find(self, val, node):
        if val == node.val:
            return True
        elif val < node.val and node.left is not None:
            return self._find(val, node.left)
        elif val > node.val and node.right is not None:
            return self._find(val, node.right)
        return False

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, node):
        if node is not None:
            self._print_tree(node.left)
            print(str(node.val) + ' ')
            self._print_tree(node.right)

    def get_max(self):
        if self.root is not None:
            return self._get_max(self.root)

    def _get_max(self, node):
        if node.right is not None:
            return self._get_max(node.right)
        return node.val

    def get_min(self):
        if self.root is not None:
            return self._get_min(self.root)

    def _get_min(self, node):
        if node.left is not None:
            return self._get_min(node.left)
        return node.val

    def delete_val(self, val):
        if self.root is not None:
            self._delete_val(self.root, val)

    def _delete_val(self, node, val):
        if val < node.val:
            node.left = self._delete_val(node.left, val)
        elif val > node.val:
            node.right = self._delete_val(node.right, val)
        else:
            if node.left is None and node.right is None:
                node = None
            elif node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            else:
                node.val = self._get_min(node.right)
                node.right = self._delete_val(node.right, node.val)
        return node

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    bst = BinaryTree()
    bst.insert(a[0])
    k = 1
    s = 'R'
    for i in range(1, n):
        if a[i] > bst.get_max():
            bst.insert(a[i])
            k += 1
            s += 'R'
        elif a[i] < bst.get_min():
            bst.insert(a[i])
            k += 1
            s += 'L'
        elif bst.find(a[i]):
            bst.delete_val(a[i])
    print(k)
    print(s)

if __name__ == '__main__':
    main()