

import sys

def main():
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")
    t = int(input())
    for i in range(t):
        n = int(input())
        a = [int(x) for x in input().split()]
        b = [0, 0]
        for j in range(n):
            if j % 2 == 0:
                b[0] += a[j]
            else:
                b[1] += a[j]
        print(n, b[0], b[1], sep = ' ')

if __name__ == "__main__":
    main()
