
import sys

sys.setrecursionlimit(10**6)

def get_input():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    return n, k, a

def solve(n, k, a):
    ans = 0
    i = 1
    while i <= n:
        if a[i-1] == 0:
            j = i
            while j <= n and a[j-1] == 0:
                j += 1
            if j - i + 1 > 2*k:
                return -1
            if j <= n:
                a[j-1] = 1
                ans += 1
            else:
                return -1
            i = j
        else:
            i += 1
    return ans

def main():
    n, k, a = get_input()
    ans = solve(n, k, a)
    print(ans)

if __name__ == '__main__':
    main()
