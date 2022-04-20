import sys
from collections import Counter


def main():
    N = int(input())
    A = list(map(int, input().split()))
    c = Counter(A)
    ans = 0
    for i in range(1, N+1):
        if c[i] == 0:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
