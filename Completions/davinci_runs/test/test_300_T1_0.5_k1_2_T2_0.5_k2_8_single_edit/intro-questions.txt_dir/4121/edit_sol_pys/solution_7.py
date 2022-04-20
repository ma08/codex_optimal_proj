


def f(a):
    return a + 1


def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(f, a))
    print(b)


if __name__ == "__main__":
    main()
