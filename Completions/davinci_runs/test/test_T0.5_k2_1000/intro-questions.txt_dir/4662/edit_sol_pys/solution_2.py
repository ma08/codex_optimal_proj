from xml.etree import ElementTree


def depth(tree, depth):
    if tree is None:
        return depth - 1
    else:
        return max(depth(tree.left, depth + 1), depth(tree.right, depth + 1))

if __name__ == '__main__':
    tree = ElementTree.fromstring(input())
    depth = depth(tree, 0)
    print(depth)
