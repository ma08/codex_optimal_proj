import sys


def solve(n, a):
    ans = 0
    for i in range(n):
        ans += a[i] // 2
    return ans
    
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))
    print(solve(n, a))
