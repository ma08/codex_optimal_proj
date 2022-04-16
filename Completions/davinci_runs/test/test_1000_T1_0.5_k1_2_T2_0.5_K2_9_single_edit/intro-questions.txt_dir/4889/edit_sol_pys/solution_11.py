

import sys

def main():
    n = int(sys.stdin.readline().strip())
    rods = []
    for i in range(n):
        rods.append(int(sys.stdin.readline().strip()))
    rods.sort()
    while len(rods) > 1:
        rods[0] += rods.pop()
        rods.sort()
    print(rods[0])

if __name__ == '__main__':
    main()
