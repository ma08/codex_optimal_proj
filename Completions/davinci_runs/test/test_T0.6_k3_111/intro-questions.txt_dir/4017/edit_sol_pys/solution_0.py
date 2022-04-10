

import sys

def main():
    n = int(sys.stdin.readline())
    if n == 2 or n == 3:
        print(0)
    else:
        a = list(map(int, sys.stdin.readline().split()))
        s = sum(a) % 2
        nice_indexes = []
        for i in range(n):
            if (s - a[i]) % 2 == 0 or (s - a[i]) % 2 == 1:
                nice_indexes.append(i + 1)
        print(len(nice_indexes))
        print(*nice_indexes)

if __name__ == "__main__":
    main()
