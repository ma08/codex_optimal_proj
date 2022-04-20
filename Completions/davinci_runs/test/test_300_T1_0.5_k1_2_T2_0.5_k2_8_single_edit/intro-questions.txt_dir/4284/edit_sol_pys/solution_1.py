
import sys

def main():
    q = int(input())
    for _ in range(q):
        k, n, a, b = map(int, input().split())
        if a <= b:
            print(-1)
            continue
        if k < a:
            print(0)
            continue
        if k >= a + b:
            print(n)
            continue
        ans = 0
        while k >= a + b:
            k -= a
            ans += 1
        if k < a:
            print(ans)
        else:
            print(ans + 1)

if __name__ == "__main__":
    main()
