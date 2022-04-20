

import sys

def main():
    triple = [int(x) for x in sys.stdin.readline().split()]
    if triple[0] == triple[1] or triple[1] == triple[2] or triple[2] == triple[0]:
        print('Yes')
    else:
        print('No')

main()
