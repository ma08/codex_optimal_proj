

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a = sorted(a)
    b = sorted(b)
    print(a, b)
    ans = 0
    for i in range(m):
        if a[i] < b[i]:
            ans += b[i]
        else:
            ans += a[i]
    print(ans)

if __name__ == '__main__':
    main()
