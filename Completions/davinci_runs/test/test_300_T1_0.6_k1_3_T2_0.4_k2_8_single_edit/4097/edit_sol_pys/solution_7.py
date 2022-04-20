


def solve(n, sequence, m):
    if m == 1:
        if sequence[0] == 0:
            return 1
        else:
            return 0
    elif m == 2:
        if sequence[0] == 0 and sequence[1] == 1:
            return 1
        else:
            return 0
    elif m == 3:
        if sequence[0] == 0 and sequence[1] == 1 and sequence[2] == 0:
            return 1
        else:
            return 0
    elif m == 4:
        if sequence[0] == 0 and sequence[1] == 1 and sequence[2] == 0 and sequence[3] == 1:
            return 1
        else:
            return 0
    elif m == 5:
        if sequence[0] == 0 and sequence[1] == 1 and sequence[2] == 0 and sequence[3] == 1 and sequence[4] == 0:
            return 1
        else:
            return 0
    elif m == 6:
        if sequence[0] == 0 and sequence[1] == 1 and sequence[2] == 0 and sequence[3] == 1 and sequence[4] == 0 and sequence[5] == 1:
            return 1
        else:
            return 0


if __name__ == '__main__':
    n = int(input())
    sequence = [int(x) for x in input()]
    print(solve(n, sequence, len(sequence)))
