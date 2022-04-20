


def main():
    n = int(input())
    string = input()

    if n == 0:
        print(0)
        return

    i = 0
    while i < n - 1:
        if string[i] == string[i + 1]:
            string = string[:i] + string[i + 1:]
            n -= 1
            i -= 1
        i += 1

    print(len(string))
    print(string)


if __name__ == "__main__":
    main()