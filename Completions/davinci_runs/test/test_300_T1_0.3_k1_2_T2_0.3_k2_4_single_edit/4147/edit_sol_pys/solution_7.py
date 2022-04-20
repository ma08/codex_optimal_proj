
import sys

def main():
    n, a, b, c = map(int, input().split())
    l = sorted([int(input()) for _ in range(n)])
    ans = float('inf')
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if l[i] < a and l[j] < b and l[k] < c: ans = min(ans, (a - l[i]) + (b - l[j]) + (c - l[k]))
    print(ans if ans != float('inf') else 'impossible')

if __name__ == '__main__':
    main()
