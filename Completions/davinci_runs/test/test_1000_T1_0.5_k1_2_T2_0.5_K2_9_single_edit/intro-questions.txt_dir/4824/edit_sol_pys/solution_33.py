

import sys

def readline():
    return sys.stdin.readline().strip()

def main():
    C, P = [int(x) for x in readline().split()]
    heights = [int(x) for x in readline().split()]

    count = 0
    for i in range(C - 1):
        if heights[i] == heights[i+1]:
            count += 1
    print(count + 1)

if __name__ == '__main__':
    main()
