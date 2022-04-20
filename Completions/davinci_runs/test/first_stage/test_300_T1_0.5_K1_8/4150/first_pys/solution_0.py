

import sys

def main():
    n, k = [int(x) for x in sys.stdin.readline().split()]
    a = [int(x) for x in sys.stdin.readline().split()]
    a_map = {a[i]: i for i in range(n)}
    a.sort()
    ans = [0] * n
    for i in range(n):
        if i % 2 == 0:
            ans[a_map[a[i]]] = 1
        else:
            ans[a_map[a[i]]] = 2
    print("".join([str(x) for x in ans]))

if __name__ == "__main__":
    main()