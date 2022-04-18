

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    a.sort()
    b.sort()
    c.sort()
    x = y = z = 0
    ans = 0
    while y < n:
        while x < n and a[x] < b[y]:
            x += 1
        while z < n and c[z] < b[y]:
            z += 1
        ans += x * z
        y += 1
    print(ans)

if __name__ == '__main__':
    main()
