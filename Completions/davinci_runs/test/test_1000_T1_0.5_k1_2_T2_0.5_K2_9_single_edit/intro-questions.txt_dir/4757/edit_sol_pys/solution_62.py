import sys
import math


def main():
    inp = sys.stdin.readlines()
    for i in range(1, len(inp), 2):
        n = int(inp[i])
        a = [int(x) for x in inp[i + 1].split()]
        a.sort()
        print(a[int(math.ceil(len(a) / 2))])

if __name__ == "__main__":
    main()
