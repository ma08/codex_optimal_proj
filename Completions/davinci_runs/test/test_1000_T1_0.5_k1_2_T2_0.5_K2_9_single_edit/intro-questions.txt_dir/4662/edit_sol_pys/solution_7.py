import xml.etree.ElementTree as etree


def depth(tree):
    if tree is None:
        return -1
    else:
        return max(depth(tree[0]), depth(tree[1])) + 1


if __name__ == '__main__':
    xml = ""
    for i in range(int(input())):
        xml = xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml.strip())).getroot()
    depth = depth(tree)
    print(depth)
