def solve(n, k, arr):
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] < k:
                ans += 1
    return ans


def main():
    n, k = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    print(solve(n, k, arr))


if __name__ == "__main__":
    main()
