

def main():
    n, m = map(int, input().split())
    a = [0] * n
    for i in range(m):
        l, r, k = map(int, input().split())
        a[l-1] += k
        if r != n:
            a[r] -= k
    ans = 0
    for i in range(n):
        ans += a[i]
        a[i] = ans
    print(max(a))


if __name__ == "__main__":
    main()
