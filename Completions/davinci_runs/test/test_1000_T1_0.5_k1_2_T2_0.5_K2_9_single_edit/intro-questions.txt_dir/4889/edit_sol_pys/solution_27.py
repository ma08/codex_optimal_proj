

import sys

def main():
    n = int(input())
    rods = []
    for i in range(n):
        rods.append(int(input()))
    rods.sort()
    total = rods[0]
    for i in range(1,n):
        total += rods[i]-1
    print(total)

if __name__ == '__main__':
    main()
