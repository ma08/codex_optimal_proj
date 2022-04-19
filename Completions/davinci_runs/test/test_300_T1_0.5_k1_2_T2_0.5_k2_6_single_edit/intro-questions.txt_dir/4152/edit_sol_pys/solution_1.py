

def solve(arr):
    memo = [0] * (2 ** 20)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] < 2 ** 20:
                memo[arr[i] + arr[j]] = 1
    return len(arr) - sum(memo)


def main():
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(solve(arr))


if __name__ == "__main__":
    main()


def solve(arr):
    memo = [set()] * (2 ** 20)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] < 2 ** 20:
                memo[arr[i] + arr[j]].add(i)
                memo[arr[i] + arr[j]].add(j)
    return len(arr) - sum(len(x) for x in memo)


def main():
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(solve(arr))


if __name__ == "__main__":
    main()


def solve(arr):
    memo = [set()] * (2 ** 20)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] < 2 ** 20:
                memo[arr[i] + arr[j]].add(i)
                memo[arr[i] + arr[j]].add(j)
    return len(arr) - sum(len(x) for x in memo)


def main():
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(solve(arr))


if __name__ == "__main__":
    main()


def solve(arr):
    memo = [False] * (2 ** 20)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] < 2 ** 20:
                memo[arr[i] + arr[j]] = True
    return len(arr) - sum(memo)


def main():
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(solve(arr))


if __name__ == "__main__":
    main()


def solve(arr):
    memo = [False] * (2 ** 20)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] < 2 ** 20:
                memo[arr[i] + arr[j]] = True
    return len(arr) - sum(memo)


def main():
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(solve(arr))


if __name__ == "__main__":
    main()


def solve(arr):
    memo = [False] * (2 ** 20)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] < 2 ** 20:
                memo[arr[i] + arr[j]] = True
    return len(arr) - sum(memo)


def main():
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(solve(arr))


if __name__ == "__main__":
    main()


def solve(arr):
    memo = [False] * (2 ** 20)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] < 2 ** 20:
                memo[arr[i] + arr[j]] = True
    return len(arr) - sum(memo)


def main():
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(solve(arr))


if __name__ == "__main__":
    main()


def solve(arr):
    memo = [False] * (2 ** 20)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] < 2 ** 20:
                memo[arr[i] + arr[j]] = True
    return len(arr) - sum(memo)


def main():
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(solve(arr))


if __name__ == "__main__":
    main()


def solve(arr):
    memo = [False] * (2 ** 20)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] < 2 ** 20:
                memo[arr[i] + arr[j]] = True
    return len(arr) - sum(memo)


def main():
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(solve(arr))


if __name__ == "__main__":
    main()


def solve(arr):
    memo = [False] * (2 ** 20)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] < 2 ** 20:
                memo[arr[i] + arr[j]] = True
    return len(arr) - sum(memo)


def main():
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(solve(arr))


if __name__ == "__main__":
    main()


def solve(arr):
    memo = [False] * (2 ** 20)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] < 2 ** 20:
                memo[arr[i] + arr[j]] = True
    return len(arr) - sum(memo)


def main():
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(solve(arr))


if __name__ == "__main__":
    main()


def solve(arr):
    memo = [False] * (2 ** 20)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] < 2 ** 20:
                memo[arr[i] + arr[j]] = True
    return len(arr) - sum(memo)


def main():
    n =

def solve(arr):
    memo = [False] * (2 ** 20)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] < 2 ** 20:
                memo[arr[i] + arr[j]] = True
    return len(arr) - sum(memo)


def main():
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(solve(arr))


if __name__ == "__main__":
    main()
