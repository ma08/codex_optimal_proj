
import collections


def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = collections.Counter(a)
    d = sorted(d.items(), key=lambda x: x[1], reverse=True)[0]
    mod = 998244353
    ans = 1
    ans = (ans * pow(2, d[1], mod)) % mod
    ans = (ans * d[1]) % mod
    print(ans)


if __name__ == "__main__":
    main()
