
def depth(tree):
    if tree is None:
        return 0
    else:
        return max(depth(tree.left) + 1, depth(tree.right) + 1)

if __name__ == '__main__':
    xml = ""
    for i in range(int(input())):
        xml =  xml + input() + "\n"
    tree = xml.strip().split()
    print(depth(tree))
