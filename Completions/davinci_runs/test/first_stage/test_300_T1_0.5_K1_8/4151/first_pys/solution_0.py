

def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        if a[i] not in d:
            d[a[i]] = 0
        d[a[i]] += 1
    ans = 1
    for i in d:
        ans *= d[i] + 1
        ans %= 998244353
    print(ans)

if __name__ == "__main__":
    main()