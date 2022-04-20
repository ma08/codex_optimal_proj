

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = [0] * n

    def get_max(a):
        m = 0
        for i in range(n):
            if a[i] > a[m]:
                m = i
        return m

    def get_min(a):
        m = 0
        for i in range(n):
            if a[i] < a[m]:
                m = i
        return m

    def get_left(m):
        return max(0, m - k)

    def get_right(m):
        return min(n - 1, m + k)

    def update(a, m, c):
        for i in range(get_left(m), get_right(m) + 1):
            if a[i] != 0:
                ans[i] = c
        return a[:get_left(m)] + a[get_right(m) + 1:]

    c = 1
    while a:
        m = get_max(a)
        a = update(a, m, c)
        c = 3 - c

    print(''.join(map(str, ans)))

if __name__ == '__main__':
    main()