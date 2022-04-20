

def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    ans = 0
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            if all(s[i + k][j + l] == t[k][l] for k in range(m) for l in range(m)):
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()
