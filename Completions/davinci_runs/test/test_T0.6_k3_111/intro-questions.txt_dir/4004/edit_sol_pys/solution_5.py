

def sum(n, a):
    return sum(a)


def min_diff(n, a):
    s = sum(n, a)
    if s % n == 0:
        return s // n
    else:
        return -1


def max_diff(n, a):
    return max(a) - min(a)


def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    print(min_diff(n, a))
    print(max_diff(n, a))


if __name__ == "__main__":
    main()
