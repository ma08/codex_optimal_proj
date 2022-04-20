
def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    ans = 1
    for i in range(1, n):
        if a[i] - a[i - 1] <= 5:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
