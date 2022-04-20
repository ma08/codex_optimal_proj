

def main():
    n, k = [int(x) for x in input().split()]
    s = input()
    if n < k:
        print(-1)
        return
    ans = 0
    for i in range(n - 1, n - k, -1):
        ans += i
    print(ans)


if __name__ == "__main__":
    main()