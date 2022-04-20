

import sys

def main():
    triple = [int(x) for x in sys.stdin.readline().split()]
    if triple[0] == triple[1] or triple[1] == triple[2] or triple[0] == triple[2]:
        print('Yes')
    else:
        print('No')

main()
