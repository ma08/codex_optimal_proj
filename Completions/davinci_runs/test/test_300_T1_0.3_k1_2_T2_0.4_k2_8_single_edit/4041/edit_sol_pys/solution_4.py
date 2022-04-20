

def main():
    s = input().split()
    n = int(s[0])
    m = int(s[1])
    a = list(map(int, input().split()))
    a.sort()
    b = list(map(int, input().split()))
    b.sort()
    c = list(map(int, input().split()))
    c.sort()
    ans = 0
    for i in range(m):
        ans += bisect_left(a, b[i]) * (n - bisect_right(c, b[i]))
    print(ans)


if __name__ == '__main__':
    main()
