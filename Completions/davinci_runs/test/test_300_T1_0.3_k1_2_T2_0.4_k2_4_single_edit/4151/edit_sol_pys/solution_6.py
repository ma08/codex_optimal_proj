

def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        if a[i] not in d:
            d[a[i]] = [i]
        else:
            d[a[i]].append(i)
    d = sorted(d.items(), key=lambda x: len(x[1]), reverse=True)
    ans = 1
    for i in d:
        ans *= (2 ** (len(i[1]) - 1))
        ans %= 998244353
    print(ans)

if __name__ == "__main__":
    main()
