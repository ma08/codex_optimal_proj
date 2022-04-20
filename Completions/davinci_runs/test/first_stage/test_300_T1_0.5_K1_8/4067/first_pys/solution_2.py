


def main():
    n = int(input())
    s = input()
    if len(set(s)) == 1:
        print(s[0] * n)
    else:
        print(s)


if __name__ == "__main__":
    main()