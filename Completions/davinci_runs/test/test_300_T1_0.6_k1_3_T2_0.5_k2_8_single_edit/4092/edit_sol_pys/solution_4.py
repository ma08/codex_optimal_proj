
def main():
    n = int(input())
    a = [int(x) for x in input().split()] + [0, 0]
    s = [0] * (n+2) + [0]
    for i in range(1, n+3):
        s[i] = s[i-1] + a[i]
    d = {0: 0}
    ans = -1
    for i in range(1, n+3):
        if s[i] in d:
            ans = max(ans, i - d[s[i]] - 1)
        d[s[i]] = i
    print(ans if ans != -1 else 0)

if __name__ == "__main__":
    main()
