def depth(tree):
    if tree is None:
        return -1
    else:
        return max(depth(tree.left), depth(tree.right)) + 1

if __name__ == '__main__':
    tree = input()
    depth = depth(tree)
    print(depth)
