import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    a.sort()
    l = 0
    r = 10**9
    while l < r:
        mid = (l + r) // 2
        cnt = 0
        for i in a:
            cnt += mid // i
        if cnt >= m:
            r = mid
        else:
            l = mid + 1
    print(l)

if __name__ == '__main__':
    main()
