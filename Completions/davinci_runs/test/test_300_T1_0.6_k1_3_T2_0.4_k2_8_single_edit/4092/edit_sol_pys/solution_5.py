
def main():
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append([int(x) for x in input().split()])
    b = []
    for i in range(m):
        b.append([int(x) for x in input().split()])
    for i in range(n):
        ans = 0
        for j in range(m):
            ans += a[i][j] * b[j][0]
        print(ans)

if __name__ == "__main__":
    main()
