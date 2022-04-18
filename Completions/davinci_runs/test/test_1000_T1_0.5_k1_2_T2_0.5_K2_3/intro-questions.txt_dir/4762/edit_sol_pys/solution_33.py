
def main():
    n = int(input())
    print(1 - (fact(n) / (fact(n - n) * fact(n))))  # (n - n) = 0


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


if __name__ == "__main__":
    main()
