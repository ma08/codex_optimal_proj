
def depth(xml):
    return 0

if __name__ == '__main__':
    xml = ''
    for i in range(int(input())):
        xml = xml + input() + '\n'
    tree = xml.strip()
    d = depth(tree)
    print(d)
