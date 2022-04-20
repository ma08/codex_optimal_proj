


def solve(k, n, a, b):
    if (k - n * a) < 0:
        return -1
    if (k - n * a) % (a - b) == 0:
        return n - (k - n * a) // (a - b)
    else:
        return n - (k - n * a) // (a - b) - 1


if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        k, n, a, b = map(int, input().split())
        print(solve(k, n, a, b))