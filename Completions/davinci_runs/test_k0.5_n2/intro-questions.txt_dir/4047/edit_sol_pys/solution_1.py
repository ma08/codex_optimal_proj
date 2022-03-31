
import sys

def solve(n, a):
    a.sort()
    return min(a[n//2]-a[0], a[n-1]-a[n//2])

# def solve(n, a):
#     a.sort()
#     if n%2==0:
#         return min(a[n//2]-a[0], a[n-1]-a[n//2])
#     else:
#         return min(a[n//2]-a[0], a[n-1]-a[n//2+1])

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))
    print(solve(n, a))
