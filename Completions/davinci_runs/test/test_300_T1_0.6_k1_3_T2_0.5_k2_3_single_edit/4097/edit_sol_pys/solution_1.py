


def solve(n, sequence, k):
    if n == 1:
        return k
    elif n == 2:
        return k
    else:
        diff = sequence[1] - sequence[0]
        i = 2
        while i < n:
            if sequence[i] - sequence[i-1] != diff:
                return k
            i += 1
        return k


if __name__ == '__main__':
    n = int(input())
    sequence = [int(x) for x in input().split()]
    k = int(input())
    print(solve(n, sequence, k))
