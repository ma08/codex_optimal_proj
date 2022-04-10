

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(1, n + 1):
        s[i] = s[i - 1] + a[i - 1]
    ans = 0
    d = {}
    for i in range(n + 1):
        if s[i] in d:
            ans = max(ans, i - d[s[i]])
        else:
            d[s[i]] = i
    print(n - ans)

if __name__ == '__main__':
    main()