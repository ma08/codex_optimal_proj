from collections import defaultdict


def solve(arr):
    memo = defaultdict(int)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            memo[arr[i] + arr[j]] += 1
    return len(arr) - max(memo.values())


def main():
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(solve(arr))


if __name__ == "__main__":
    main()
