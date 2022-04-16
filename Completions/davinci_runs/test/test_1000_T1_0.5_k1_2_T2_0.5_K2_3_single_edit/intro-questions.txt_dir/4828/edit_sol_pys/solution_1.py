


def solve(s):
    n = 0
    for i in range(len(s)):
        if (i % 4 == 0) and (s[i].isupper()):
            pass
        else:
            n += 1
    return n


def main():
    n = int(input())
    for i in range(n):
        print("Case #{}: {}".format(i + 1, solve(input())))
    return

    s = input()
    print(solve(s))


if __name__ == "__main__":
    main()
