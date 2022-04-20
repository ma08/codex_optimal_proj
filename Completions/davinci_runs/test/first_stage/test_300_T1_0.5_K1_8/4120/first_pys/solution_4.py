

# Use this class to create binary trees
class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    # Use this function to add a new node to the binary tree
    def add(self, val):
        if val <= self.value:
            if self.left is None:
                self.left = Node(val, self)
            else:
                self.left.add(val)
        else:
            if self.right is None:
                self.right = Node(val, self)
            else:
                self.right.add(val)

    def get_min(self):
        if self.left is None:
            return self
        else:
            return self.left.get_min()

    # Use this function to check if a node exists in the binary tree
    def exists(self, val):
        if val == self.value:
            return True
        elif val < self.value:
            if self.left is None:
                return False
            else:
                return self.left.exists(val)
        else:
            if self.right is None:
                return False
            else:
                return self.right.exists(val)

    # Use this function to remove a node from the binary tree
    def remove(self, val, parent):
        if val < self.value:
            if self.left is not None:
                self.left.remove(val, self)
        elif val > self.value:
            if self.right is not None:
                self.right.remove(val, self)
        else:
            if self.left is not None and self.right is not None:
                self.value = self.right.get_min().value
                self.right.remove(self.value, self)
            elif parent.left == self:
                if self.left is not None:
                    temp = self.left
                else:
                    temp = self.right
                parent.left = temp
            elif parent.right == self:
                if self.left is not None:
                    temp = self.left
                else:
                    temp = self.right
                parent.right = temp


# Use this function to check if a binary tree is a BST
def is_bst(root):
    if root is None:
        return True
    if root.left is not None and root.left.value > root.value:
        return False
    if root.right is not None and root.right.value < root.value:
        return False
    if not is_bst(root.left) or not is_bst(root.right):
        return False
    return True


def main():
    # Read input
    n, m, k = [int(i) for i in input().split()]

    # Create a binary tree with the first value
    root = Node(int(input().split()[0]), None)

    # Add the rest of the values to the binary tree
    for i in range(n - 1):
        root.add(int(input().split()[0]))

    # Check if the binary tree is a BST
    if is_bst(root):
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()