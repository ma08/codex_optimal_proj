


def main():
    n = int(input())
    s = input()
    if n % 2 == 1:
        print(n)
        print(s)
    else:
        k = 0
        for i in range(0, n, 2):
            if s[i] == s[i + 1]:
                k += 1
        print(k)
        for i in range(0, n, 2):
            if s[i] != s[i + 1]:
                print(s[i], end="")
        print()


if __name__ == "__main__":
    main()