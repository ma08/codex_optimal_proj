
import sys

def main():
    x, n = map(int, sys.stdin.readline().split())
    p = list(map(int, sys.stdin.readline().split()))
    p.sort()
    ans = 0
    if x < p[0]:
        ans = p[0] - x
    elif x > p[-1]:
        ans = x - p[-1]
    else:
        for i in range(n):
            if x < p[i]:
                ans = min(ans, p[i] - x)
                break
            ans = min(ans, x - p[i])
    print(ans)

if __name__ == '__main__':
    main()
