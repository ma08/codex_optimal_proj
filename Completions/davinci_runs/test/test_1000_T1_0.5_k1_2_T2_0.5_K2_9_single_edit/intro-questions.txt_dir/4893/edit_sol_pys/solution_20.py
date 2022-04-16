
def main():
    n, p = map(int, input().split())
    d = sorted([int(x) for x in input().split()])
    ans = d[0]
    for i in range(1, n - 1):
        if d[i + 1] - d[i - 1] < p * 2:
            ans = d[i - 1] + p
    if d[n - 1] - d[n - 2] < p:
        ans = d[n - 2] + p
    print(ans)

if __name__ == "__main__":
    main()
