

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    a.sort()
    b.sort()
    c.sort()
    ans = 0
    for i in range(n):
        bi = b[i]
        ai = bisect.bisect_left(a, bi)
        ci = bisect.bisect_right(c, bi)
        ans += ai * (n - ci)
    print(ans)

if __name__ == '__main__':
    main()
