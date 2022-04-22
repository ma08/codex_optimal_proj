

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

def print_tree(root):
    if root.left:
        print_tree(root.left)
    print(root)
    if root.right:
        print_tree(root.right)

if __name__ == '__main__':
    n = Node(1)
    n.left = Node(2)
    n.right = Node(3)
    n.left.left = Node(4)
    n.left.right = Node(5)
    n.right.left = Node(6)
    n.right.right = Node(7)
    print_tree(n)
