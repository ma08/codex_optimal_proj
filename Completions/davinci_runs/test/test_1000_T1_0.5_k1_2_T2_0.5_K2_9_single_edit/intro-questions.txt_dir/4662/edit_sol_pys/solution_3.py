
def depth(tree):
    if tree is None:
        return -1
    else:
        return max(depth(tree.left), depth(tree.right)) + 1

if __name__ == '__main__':
    tree = ""
    for i in range(int(input())):
        tree = tree + input() + "\n"
    tree = tree.strip()
    depth = depth(tree)
    print(depth)
