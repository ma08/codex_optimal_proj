def depth(tree):
    if tree is None:
        return -1
    else:
        return max(depth(tree.left), depth(tree.right)) + 1

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def parse(tree):
    if tree == "":
        return None
    else:
        node = Node(tree[0])
        left_bracket = tree.find("(")
        if left_bracket == -1:
            return node
        else:
            left_subtree = tree[left_bracket + 1:tree.find(")")]
            node.left = parse(left_subtree)
            return node

if __name__ == '__main__':
    tree = ""
    for i in range(int(input())):
        tree =  tree + input() + "\n"
    tree = tree.strip()
    tree = parse(tree)
    depth = depth(tree.left)
    print(depth)
