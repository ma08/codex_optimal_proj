
import sys

def main():
    q = int(sys.stdin.readline())
    for _ in range(q):
        k, n, a, b = map(int, sys.stdin.readline().split())
        if a <= b:
            print(-1, end='\n')
            continue
        if k <= a:
            print(0, end='\n')
            continue
        if k > a + b:
            print(n, end='\n')
            continue
        ans = 0
        while k > a + b:
            k -= a
            ans += 1
        if k <= a:
            print(ans, end='\n')
        else:
            print(ans + 1, end='\n')

if __name__ == "__main__":
    main()
