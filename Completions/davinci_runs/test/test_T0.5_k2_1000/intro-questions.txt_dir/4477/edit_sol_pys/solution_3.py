
import sys

def solve(x):
    ans = 0
    for i in range(1, x // 10 + 1):
        ans += i * (9 - x // (10**i) % 10)
    return ans

def main():
    t = int(sys.stdin.readline())
    for i in range(t):
        x = int(sys.stdin.readline())
        print(solve(x))

if __name__ == "__main__":
    main()
