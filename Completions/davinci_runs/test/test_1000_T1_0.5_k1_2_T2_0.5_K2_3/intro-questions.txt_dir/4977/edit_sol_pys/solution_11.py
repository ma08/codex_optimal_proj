
def main():
    a, b, c, d, t = map(int, input().split())

    if (a - c) ** 2 + (b - d) ** 2 == t ** 2:
        print("Y")
    else:
        print("N")


if __name__ == "__main__":
    main()
