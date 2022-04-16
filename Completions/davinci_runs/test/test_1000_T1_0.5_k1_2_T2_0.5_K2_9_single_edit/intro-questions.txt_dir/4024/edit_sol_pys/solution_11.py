

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    a.sort()
    b.sort()
    c.sort()
    p = 0
    q = 0
    r = 0
    ans = 0
    for i in range(n):
        while p < n and a[p] < b[i]:
            p += 1
        while q < n and b[i] > c[q]:
            q += 1
        ans += p * (n - q)
    print(ans)

if __name__ == '__main__':
    main()
