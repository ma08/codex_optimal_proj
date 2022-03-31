

def sum(a):
    s = 0
    for i in a:
        s += i
    return s


def min_d(n, a):
    s = sum(a)
    if s % n == 0:
        return s // n
    else:
        return -1


def max_d(n, a):
    a.sort(reverse=True)
    m = a[0]
    d = m - a[-1]
    return d


def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    print(min_d(n, a))
    # print(max_d(n, a))


if __name__ == "__main__":
    main()