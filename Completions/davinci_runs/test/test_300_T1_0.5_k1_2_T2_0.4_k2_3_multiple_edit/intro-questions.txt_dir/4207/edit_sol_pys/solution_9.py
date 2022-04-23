import bisect

def solve(n, a, b):
    a.sort()
    b.sort()
    ans = 0
    for i in range(n):
        a_idx = bisect.bisect_left(a, b[i])
        ans += n - a_idx
    return ans


if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    print(solve(n, a, b))
