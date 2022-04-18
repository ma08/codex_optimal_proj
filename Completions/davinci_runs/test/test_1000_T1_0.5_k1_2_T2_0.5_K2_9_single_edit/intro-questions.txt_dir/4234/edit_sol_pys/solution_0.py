import sys
import math



def main(n, k):
    a = [0] * k
    for i in range(k):
        a[i] = int(input())
    a.sort()
    ans = math.inf
    for i in range(k-n+1):
        ans = min(ans, a[i+n-1] - a[i])
    print(ans)

if __name__ == '__main__':
    n, k = map(int, input().split())
    main(n, k)
