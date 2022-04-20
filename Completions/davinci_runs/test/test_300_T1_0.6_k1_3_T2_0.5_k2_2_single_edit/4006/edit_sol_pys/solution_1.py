
def f(n):
    if n % 10 == 0:
        return f(n // 10)
    else:
        return n + 1


def r(n, d=0):
    s = set([])
    while n not in s:
        s.add(n)
        n = f(n)
    if d:
        return len(s)
    return s


def main():
    n, k = map(int, input().split())
    s = r(n)
    for i in range(k):
        m = int(input())
        if m in s:
            print(m, len(s))
        else:
            print(m, r(m, 1))


if __name__ == "__main__":
    main()
