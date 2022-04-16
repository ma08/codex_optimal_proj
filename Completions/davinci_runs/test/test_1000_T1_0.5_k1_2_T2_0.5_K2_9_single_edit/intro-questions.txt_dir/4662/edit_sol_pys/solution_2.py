
def depth(tree):
    if tree is None:
        return -1
    return max(depth(tree.left), depth(tree.right)) + 1

if __name__ == '__main__':
    xml = ""
    for i in range(int(input())):
        xml += input() + "\n"
    tree = xml.strip()
    depth = depth(tree)
    print(depth)
