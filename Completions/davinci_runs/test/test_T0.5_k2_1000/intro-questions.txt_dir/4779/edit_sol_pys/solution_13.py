
import sys

def main():
    n = int(sys.stdin.readline())
    a = [int(sys.stdin.readline()) for i in range(n)]
    a.sort()
    ans, cur = 0, 0
    for i in range(n): cur += a[i]; ans = max(ans, cur * a[i])
    print(ans)

if __name__ == '__main__':
    main()
