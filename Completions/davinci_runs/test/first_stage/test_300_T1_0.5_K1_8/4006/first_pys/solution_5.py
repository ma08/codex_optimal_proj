


def main():
    n = int(input())
    print(solve(n))


def solve(n):
    s = set()
    for i in range(1, 10):
        s.add(i)
        if i == n:
            return len(s)
    while True:
        s2 = set()
        for i in s:
            if i % 10 != 0:
                s2.add(i + 1)
            s2.add(i * 10 + 1)
        s = s2
        if n in s:
            return len(s)


if __name__ == "__main__":
    main()