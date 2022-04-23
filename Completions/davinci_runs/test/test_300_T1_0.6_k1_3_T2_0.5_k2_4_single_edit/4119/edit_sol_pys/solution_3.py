


def main():
    N, M = map(int, input().split())
    X = sorted(list(map(int, input().split())))
    X_min = X[0] - 1
    X_max = X[-1] + 1
    total = 0
    for i in range(M):
        total += abs(X[i] - X_min)
    for i in range(M):
        total += abs(X[i] - X_max)
    print(total)


if __name__ == '__main__':
    main()
