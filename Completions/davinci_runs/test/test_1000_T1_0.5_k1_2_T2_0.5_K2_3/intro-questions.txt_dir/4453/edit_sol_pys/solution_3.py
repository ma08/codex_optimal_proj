

from sys import stdin

def main():
    q = int(input())
    for _ in range(q):
        n = int(input())
        p = list(map(int, stdin.readline().split()))[:n]
        a = list(range(1, n+1))
        ans = [0] * n
        for i in range(n):
            while a[i] != i+1:
                a[i], a[p[i]-1] = a[p[i]-1], a[i]
                ans[i] += 1
        print(*ans)


if __name__ == "__main__":
    main()
