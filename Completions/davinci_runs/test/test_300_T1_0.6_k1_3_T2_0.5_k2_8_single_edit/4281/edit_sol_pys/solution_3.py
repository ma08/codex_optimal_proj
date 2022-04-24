


def main():
    n = int(input())
    x = list(map(int, input().split()))

    idxs = [[] for _ in range(n + 1)]
    for i, xi in enumerate(x):
        idxs[xi].append(i)

    min_p = max_p = 0
    for i, idx in enumerate(idxs):
        if len(idx) > 0:
            min_p += 1
            max_p += 1

            if i == 0:
                max_p += len(idx) - 1
            elif i == n:
                max_p += len(idx) - 1
            else:
                max_p += len(idx)

    print(min_p, max_p)


if __name__ == '__main__':
    main()
