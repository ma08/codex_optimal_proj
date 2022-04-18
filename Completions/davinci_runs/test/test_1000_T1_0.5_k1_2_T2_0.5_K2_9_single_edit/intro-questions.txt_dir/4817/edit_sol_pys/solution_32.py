

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    a.sort()
    b.sort()
    c.sort()

    ans = 0
    for i in range(m):
        a_index = bisect_right(a, b[i])
        c_index = bisect_left(c, b[i])
        ans += a_index * (n - c_index)
    print(ans)

if __name__ == "__main__":
    main()
