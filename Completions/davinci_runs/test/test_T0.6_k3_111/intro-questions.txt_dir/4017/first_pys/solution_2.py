

import sys

def main():
    n = int(sys.stdin.readline())
    if n == 2:
        print(0)
    else:
        a = list(map(int, sys.stdin.readline().split()))
        s = sum(a)
        nice_indices = []
        for i in range(n):
            if (s - a[i]) % 2 == 0:
                nice_indices.append(i + 1)
        print(len(nice_indices))
        print(*nice_indices)

if __name__ == "__main__":
    main()