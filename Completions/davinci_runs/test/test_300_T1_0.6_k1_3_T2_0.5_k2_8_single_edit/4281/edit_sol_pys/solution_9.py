

def calc_min_p(idxs):
    min_p = 0
    for idx in idxs:
        if len(idx) > 0:
            min_p += 1
    return min_p


def calc_max_p(idxs, n):
    max_p = 0
    for i, idx in enumerate(idxs):
        if len(idx) > 0:
            max_p += 1

            if i == 0:
                max_p += len(idx) - 1
            elif i == n:
                max_p += len(idx) - 1
            else:
                max_p += len(idx)
    return max_p



def main():
    n = int(input())
    x = list(map(int, input().split()))

    idxs = [[] for _ in range(n+1)]
    for i, xi in enumerate(x):
        idxs[xi].append(i)

    min_p = calc_min_p(idxs)
    max_p = calc_max_p(idxs, n)

    print(min_p, max_p)


if __name__ == '__main__':
    main()
