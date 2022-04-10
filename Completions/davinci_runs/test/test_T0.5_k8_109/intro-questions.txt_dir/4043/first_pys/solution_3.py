

n, d, k = map(int, input().split())


def solve(n, d, k):
    if d == 1:
        return "YES\n1 2\n" + "\n".join(["2 " + str(i + 3) for i in range(n - 2)])
    if d == 2:
        if k >= n - 1:
            return "YES\n1 2\n" + "\n".join(
                ["1 " + str(i + 3) for i in range(n - 2)]
            )
        else:
            return "NO"
    if d == 3:
        if k >= n - 2:
            return "YES\n1 2\n" + "\n".join(
                ["1 " + str(i + 3) for i in range(n - 2)]
            )
        else:
            return "NO"
    if d == 4:
        if k >= n - 3:
            return "YES\n1 2\n" + "\n".join(
                ["1 " + str(i + 3) for i in range(n - 2)]
            )
        else:
            return "NO"


print(solve(n, d, k))