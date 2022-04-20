
def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))  # a = [int(i) for i in input().split()]
    a.sort()

    ans = 0
    for i in range(n):
        for j in range(i, n):
            if a[j] - a[i] <= k:
                ans = max(ans, j - i + 1)

            else:
                break

    print(ans)

if __name__ == '__main__':
    main()
