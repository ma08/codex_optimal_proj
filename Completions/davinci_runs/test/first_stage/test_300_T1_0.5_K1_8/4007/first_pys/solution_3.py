

def main():
    n = int(input().strip())
    f = list(map(int, input().strip().split()))
    assert n == len(f)

    # There are two cases:
    #   1. There are only two 0's, in which case we can simply swap them
    #   2. There are more than two 0's, in which case we can assign the 0's
    #      in a round robin fashion

    zeros = []
    for i in range(n):
        if f[i] == 0:
            zeros.append(i)

    if len(zeros) == 2:
        f[zeros[0]], f[zeros[1]] = f[zeros[1]], f[zeros[0]]
    else:
        i = 0
        for j in range(n):
            if f[j] == 0:
                f[j] = zeros[i] + 1
                i += 1

    print(' '.join(map(str, f)))


if __name__ == "__main__":
    main()