from itertools import product


def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]

    k = [0]
    for i, j in product(range(n), range(n)):
        if i == j:
            continue
        for c in range(m):
            k.append(abs(a[i][c] - a[j][c]))

    print(max(k))


if __name__ == "__main__":
    main()
