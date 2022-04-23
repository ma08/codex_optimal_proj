


def main():
    d, n = list(map(int, input().split()))
    if d == 0:
        print(n)
    elif d == 1:
        print(n * 100 + n)
    else:
        print(n * 100 + n * 10)

if __name__ == "__main__":
    main()
