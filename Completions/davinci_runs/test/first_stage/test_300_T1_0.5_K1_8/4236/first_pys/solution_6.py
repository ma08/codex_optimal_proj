


def get_input():
    n, m = map(int, input().split())
    lr = [list(map(int, input().split())) for _ in range(n)]
    return n, m, lr


def get_points(n, m, lr):
    points = set(range(m+1))
    for l, r in lr:
        points -= set(range(l, r+1))
    return points


def print_points(points):
    print(len(points))
    print(*sorted(points))


def main():
    n, m, lr = get_input()
    points = get_points(n, m, lr)
    print_points(points)


if __name__ == "__main__":
    main()