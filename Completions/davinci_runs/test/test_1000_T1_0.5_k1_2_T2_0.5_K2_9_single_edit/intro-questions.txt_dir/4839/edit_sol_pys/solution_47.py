
import math
import sys

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    ans = 0
    for i in range(n):
        for j in range(m):
            if b[j] >= a[i]:
                ans += 1
                b.pop(j)
                break
    print(ans)

if __name__ == "__main__":
    main()
