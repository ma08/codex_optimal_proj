
def solve(n, a):
    a.sort()    
    return min(a[-1] - a[1], a[-2] - a[0]) if n > 2 else 0


def main():
    n, *a = map(int, open(0).read().split())
    print(solve(n, a))


if __name__ == "__main__":
    main()
