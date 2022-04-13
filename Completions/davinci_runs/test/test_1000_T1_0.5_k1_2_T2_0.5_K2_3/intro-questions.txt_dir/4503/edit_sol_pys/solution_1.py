
import sys
from collections import deque

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    ans = 0
    for i in range(1, n, 2):
        ans += a[i]
    print(ans)

if __name__ == '__main__':
    main()
