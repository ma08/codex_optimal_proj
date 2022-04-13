import sys
import xml.etree.ElementTree as ET

def get_attr_number(node):
    return len(node.attrib) + sum([get_attr_number(child) for child in node])

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = ET.ElementTree(ET.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
