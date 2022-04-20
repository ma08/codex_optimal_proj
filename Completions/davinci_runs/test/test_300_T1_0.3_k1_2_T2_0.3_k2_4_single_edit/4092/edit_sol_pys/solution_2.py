

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = [0] * (n + 2)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    d = {}
    ans = 0
    for i in range(n + 2):
        if s[i] in d:
            ans = max(ans, i - d[s[i]])
        else:
            d[s[i]] = i
    print(n - ans)

if __name__ == '__main__':
    main()
