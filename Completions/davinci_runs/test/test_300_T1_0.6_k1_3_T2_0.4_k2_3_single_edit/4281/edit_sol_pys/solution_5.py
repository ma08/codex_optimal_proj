
from collections import defaultdict


def main():
    n = int(input())
    x = list(map(int, input().split()))

    idxs = defaultdict(list)
    for i, xi in enumerate(x):
        idxs[xi - 1].append(i)

    min_p = max_p = 0
    for i, idx in idxs.items():
        if len(idx) > 0:
            min_p += 1
            max_p += 1

            if i == 0:
                max_p += len(idx) - 1
            elif i == n - 1:
                max_p += len(idx) - 1
            else:
                max_p += len(idx)

    print(min_p, max_p)


if __name__ == '__main__':
    main()
