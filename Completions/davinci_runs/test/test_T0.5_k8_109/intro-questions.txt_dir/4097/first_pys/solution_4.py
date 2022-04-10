


def is_arithmetic_progression(seq):
    if len(seq) == 1:
        return True
    diff = seq[1] - seq[0]
    for i in range(2, len(seq)):
        if seq[i] - seq[i-1] != diff:
            return False
    return True


def min_change_to_arithmetic_progression(seq):
    if len(seq) <= 2:
        return 0
    diff = seq[1] - seq[0]
    for i in range(2, len(seq)):
        if seq[i] - seq[i-1] != diff:
            return min(min_change_to_arithmetic_progression(seq[:i-1] + [seq[i-1]+1] + seq[i:]),
                       min_change_to_arithmetic_progression(seq[:i-1] + [seq[i-1]-1] + seq[i:]),
                       min_change_to_arithmetic_progression(seq[:i-1] + [seq[i-1]] + seq[i:]),
                       min_change_to_arithmetic_progression(seq[:i-2] + [seq[i-2]+1] + seq[i-1:]),
                       min_change_to_arithmetic_progression(seq[:i-2] + [seq[i-2]-1] + seq[i-1:]),
                       min_change_to_arithmetic_progression(seq[:i-2] + [seq[i-2]] + seq[i-1:])) + 1
    return 0


def main():
    n = int(input())
    b = list(map(int, input().split()))
    if is_arithmetic_progression(b):
        print(0)
    else:
        print(min_change_to_arithmetic_progression(b))


if __name__ == '__main__':
    main()