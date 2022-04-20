

def main():
    n = int(input())
    a = list(map(int, input().split()))

    d = {}
    for i in range(n):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1

    ans = 0
    for i in range(1, 150001):
        if i in d:
            ans += 1
        if i - 1 in d:
            d[i - 1] -= d[i]
            if d[i - 1] == 0:
                del d[i - 1]

    print(ans)

if __name__ == "__main__":
    main()