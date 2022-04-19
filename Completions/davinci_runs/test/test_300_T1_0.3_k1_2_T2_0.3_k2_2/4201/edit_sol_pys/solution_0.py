
import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    a.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] + a[j] == k:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()
