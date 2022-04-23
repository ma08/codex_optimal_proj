def solve(n, k, t):
    def check(s):
        return s.count(t) == k

    if n == 1:
        return t * k

    if k == 1:
        return t

    if n == 2:
        return t * (k // 2) + t[:k % 2]

    if n == 3:
        if k <= 2:
            return t * k

        if k % 2 == 0:
            return t * (k // 2)

        if k % 3 == 0:
            return t * (k // 3)

        return t[:2] * (k // 3) + t[:k % 3]

    if n == 4:
        if k <= 2:
            return t * k

        if k % 2 == 0:
            return t * (k // 2)

        if k % 3 == 0:
            return t * (k // 3)

        if k % 4 == 0:
            return t * (k // 4)

        if k % 4 == 1:
            return t[:2] * (k // 4) + t[:1]

        if k % 4 == 2:
            return t[:2] * (k // 4) + t[:2]

        return t[:2] * (k // 4) + t[:3]

    if k % (n - 1) == 0:
        return t[:n - 1] * (k // (n - 1)) + t[:1]

    if k % n == 0:
        return t * (k // n)

    if k % (n + 1) == 0:
        return t[:n] * (k // (n + 1)) + t[:1]

    if k % (n - 1) == 1:
        return t[:n - 1] * (k // (n - 1)) + t[:2]

    if k % n == 1:
        return t[:n] * (k // n) + t[:1]

    if k % (n + 1) == 1:
        return t[:n] * (k // (n + 1)) + t[:2]

    if k % (n - 1) == 2:
        return t[:n - 1] * (k // (n - 1)) + t[:3]

    if k % n == 2:
        return t[:n] * (k // n) + t[:2]

    if k % (n + 1) == 2:
        return t[:n] * (k // (n + 1)) + t[:3]

    if k % (n - 1) == 3:
        return t[:n - 1] * (k // (n - 1)) + t[:4]

    if k % n == 3:
        return t[:n] * (k // n) + t[:3]

    if k % (n + 1) == 3:
        return t[:n] * (k // (n + 1)) + t[:4]

    return t * (k // n) + t[:k % n]


if __name__ == '__main__':
    n, k = map(int, input().split())
    t = input()

    s = solve(n, k, t)

    print(s)
