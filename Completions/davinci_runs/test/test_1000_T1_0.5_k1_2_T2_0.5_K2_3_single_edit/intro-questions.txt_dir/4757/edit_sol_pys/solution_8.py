

import sys

def main():
    n,m = [int(x) for x in sys.stdin.readline().split()]
    for i in range(m):
        line = [int(x) for x in sys.stdin.readline().split()]
        if line[0] == 1:
            print(' '.join([str(x) for x in line[1:]]))
        else:
            print(line[1])

main()
