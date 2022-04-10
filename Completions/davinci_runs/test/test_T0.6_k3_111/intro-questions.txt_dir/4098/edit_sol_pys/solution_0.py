

def main():
    n, k = map(int, input().split())
    s = list(map(int, input().split()))

    d = {}
    for i in s:
        d[i] = d.get(i, 0) + 1

    for i in range(1, k + 1):
        for j in range(i):
            if d.get(i - j, 0) > 0 and d.get(i + j, 0) > 0:
                d[i - j] -= 1
                d[i + j] -= 1
                d[i] = d.get(i, 0) + 2

    ans = 0
    for i in d.values():
        ans += i // 2

    print(min(ans, k))

if __name__ == "__main__":
    main()
