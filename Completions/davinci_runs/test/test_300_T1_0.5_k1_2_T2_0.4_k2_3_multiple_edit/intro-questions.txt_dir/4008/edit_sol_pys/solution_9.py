# https://codeforces.com/contest/1348/problem/C


def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = 0
    for i in range(n - 1):
        if a[i] == a[i + 1]:
            ans += c[a[i] - 1]
        else:
            ans += b[a[i] - 1]
    print(ans)


if __name__ == '__main__':
    main()
