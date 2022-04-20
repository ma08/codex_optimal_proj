import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    a.sort()
    b.sort()
    ans = 0
    for i in range(n):
        for j in range(m):
            if a[i] < b[j]:
                ans += 1
                b.pop(j)
                break
    print(ans)

if __name__ == '__main__':
    main()
