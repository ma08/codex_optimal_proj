

import sys

def main():
    triple = [int(x) for x in sys.stdin.readline().split()]
    if triple[0] == triple[1]:
        if triple[1] == triple[2]:
            print('Yes')
        else:
            print('No')
    elif triple[0] == triple[2]:
        if triple[2] == triple[1]:
            print('Yes')
        else:
            print('No')
    elif triple[1] == triple[2]:
        if triple[2] == triple[0]:
            print('Yes')
        else:
            print('No')

main()
