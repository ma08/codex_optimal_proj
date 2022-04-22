


def solve(arr):
    memo = [False] * (2 ** 20)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] < 2 ** 20:
                memo[arr[i] + arr[j]] = True
    return len(arr) - sum(memo)


def main():
    with open('input.txt', 'r') as f:
        n = int(f.readline())
        arr = [int(x) for x in f.readline().split()]
    print(solve(arr))


if __name__ == "__main__":
    main()
