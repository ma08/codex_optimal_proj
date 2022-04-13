

import sys

def solve(n):
    if n < 10:
        return 0
    ans = 0
    for i in range(1, n // 10 + 1):
        ans += i * (9 - n//(10**i)%10 + 1)
    return ans

def main():
    t = int(sys.stdin.readline())
    for i in range(t):
        n = int(sys.stdin.readline())
        print(solve(n))

if __name__ == "__main__":
    main()
