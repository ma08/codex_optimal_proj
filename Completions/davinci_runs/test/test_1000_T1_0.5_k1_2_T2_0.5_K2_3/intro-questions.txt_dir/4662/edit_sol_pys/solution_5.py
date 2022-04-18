import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    level += 1
    if level > maxdepth:
        maxdepth = level
    for child in elem:
        depth(child, level)


if __name__ == '__main__':
    for i in range(int(input())):
        xml = input()
        tree = etree.ElementTree(etree.fromstring(xml))
        depth(tree.getroot(), -1)
        print(maxdepth)
