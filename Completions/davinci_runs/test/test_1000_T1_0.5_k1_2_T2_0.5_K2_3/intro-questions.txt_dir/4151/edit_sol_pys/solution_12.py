

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    cnt = 1
    l = []
    for i in range(1, n):
        if a[i] == a[i - 1]:
            cnt += 1
        else:
            l.append(cnt)
            cnt = 1
    l.append(cnt)
    mod = 998244353
    ans = 1
    for i in range(len(l)):
        if i == 0:
            ans = (ans * pow(2, l[i], mod)) % mod
        else:
            ans = (ans * pow(2, l[i], mod) - 1) % mod
    print(ans)


if __name__ == "__main__":
    main()
