
import sys
sys.setrecursionlimit(1000000)

def main():
    n, m = map(int, input().split())
    a = [int(input()) for _ in range(n)]
    a.sort()
    total = sum(a)

    def check(x):
        ret = 0
        for i in range(n):
            if a[i] > x:
                ret += a[i] - x
        return ret >= m

    def meguru_bisect(ng, ok):
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if check(mid):
                ok = mid
            else:
                ng = mid
        return ok

    print(meguru_bisect(0, total))


if __name__ == "__main__":
    main()
