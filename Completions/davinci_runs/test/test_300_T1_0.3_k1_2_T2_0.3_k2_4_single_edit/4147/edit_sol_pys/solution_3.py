
import sys

def main():
    n, a, b, c = map(int, sys.stdin.readline().split())
    l = [int(sys.stdin.readline()) for _ in range(n)]
    l.sort(reverse=True)
    ans = float("inf")
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if l[i] < a and l[j] < b and l[k] < c and l[i] > l[j] and l[j] > l[k]:
                    ans = min(ans, (a - l[i]) + (b - l[j]) + (c - l[k]) + 10*(i+j+k))
    print(ans)

if __name__ == '__main__':
    main()
