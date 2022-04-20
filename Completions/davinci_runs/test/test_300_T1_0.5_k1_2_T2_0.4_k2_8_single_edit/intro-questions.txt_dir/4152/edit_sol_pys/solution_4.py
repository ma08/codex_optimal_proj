
def solve(arr):
    memo = [False] * (2 ** 20)
    for i in range(len(arr)-1):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] < 2**20:
                memo[arr[i] + arr[j]] = True
    return len(arr) - sum(memo)


def main():
    n = int(input())
    arr = [int(x) for x in input().split()][:n]
    print(solve(arr))


if __name__ == "__main__":
    main()
