


def solve(n, sequence, diff):
    if n == 1:
        return 0
    elif n == 2:
        return 0
    else:
        i = 2
        while i < n:
            if sequence[i] - sequence[i-1] != diff:
                return -1
            i += 1
        return 0


if __name__ == '__main__':
    n = int(input())
    sequence = [int(x) for x in input().split()]
    diff = sequence[1] - sequence[0]
    print(solve(n, sequence, diff))
