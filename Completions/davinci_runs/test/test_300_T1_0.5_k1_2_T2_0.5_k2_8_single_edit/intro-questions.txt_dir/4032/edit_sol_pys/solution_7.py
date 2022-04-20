
import sys
sys.setrecursionlimit(10**6)
 

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    a.sort()
    c.sort()
    ans = [0] * n
    for i, bi in enumerate(b):
        ans[i] += bisect_left(a, bi)
        ans[i] += n - bisect_right(c, bi)
    print(*ans)

if __name__ == '__main__':
    main()
