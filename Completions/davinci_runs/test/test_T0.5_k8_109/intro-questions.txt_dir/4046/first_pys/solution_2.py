


def check(x, y):
    for i in range(len(y)):
        if y[i] != x[i + 1] - x[i]:
            return False
    return True


def solve(n, y):
    x = [0] * (n + 1)
    x[0] = y[0]
    for i in range(1, n):
        if x[i - 1] + y[i] > 0:
            x[i] = x[i - 1] + y[i]
        else:
            x[i] = 1
    if x[n - 1] + y[-1] > 0:
        x[n] = x[n - 1] + y[-1]
    else:
        x[n] = 1
    if check(x, y):
        return ' '.join(str(i) for i in x[1:])
    else:
        return -1


if __name__ == '__main__':
    n = int(input())
    y = list(map(int, input().split()))
    print(solve(n, y))