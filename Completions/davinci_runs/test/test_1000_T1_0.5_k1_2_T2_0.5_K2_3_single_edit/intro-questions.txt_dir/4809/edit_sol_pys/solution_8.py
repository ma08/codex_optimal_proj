
def coconut_splat(s, n):
    if s == 9:
        return (n - 1) % 2 + 1
    else:
        return (n - 1) % 3 + 1


def main():
    s, n = map(int, input().split())
    print(coconut_splat(s, n))


if __name__ == "__main__":
    main()
