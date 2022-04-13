

def solve(n, a):
    a.sort()
    if n == 2:
        return 0
    if a[0] + 1 == a[1]:
        return a[-1] - a[1]
    if a[-1] - 1 == a[-2]:
        return a[-1] - a[0]
    return min(a[-1] - a[1], a[-2] - a[0])


def main():
    n, *a = map(int, open(0).read().split())
    print(solve(n, a))


if __name__ == "__main__":
    main()
