
import sys

def main():
    q = int(sys.stdin.readline())
    for _ in range(q):
        k, n, a, b = map(int, sys.stdin.readline().split())
        if a <= b:
            print(-1)
            continue
        if k < a:
            print(0)
            continue
        if k >= a + b * (n - 1):
            print(n)
            continue
        ans = 0
        while k >= a + b * (n - 1):
            k -= a
            ans += 1
        print(ans)

if __name__ == "__main__":
    main()
