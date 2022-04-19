
import sys

def main():
    n, a, b, c = map(int, input().split())
    l = sorted([int(input()) for _ in range(n)])
    ans = 10**9
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if l[i] < a and l[j] < b and l[k] < c:
                    ans = min(ans, (a - l[i]) + (b - l[j]) + (c - l[k]) + (l[i] + l[j] + l[k] - a - b - c))
    print(ans if ans != 10**9 else 0)

if __name__ == '__main__':
    main()
