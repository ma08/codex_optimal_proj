

def sum(a):
    s = 0
    for i in a:
        s += i
    return s


def min_diff(n, a):
    s = sum(a)
    if s % n == 0:
        return s // n
    else:
        return -1


def max_diff(n, a):
    a.sort()
    m = a[-1]
    d = m - a[0]
    return d + 1


def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    print(min_diff(n, a))
    print(max_diff(n, a))


if __name__ == "__main__":
    main()
