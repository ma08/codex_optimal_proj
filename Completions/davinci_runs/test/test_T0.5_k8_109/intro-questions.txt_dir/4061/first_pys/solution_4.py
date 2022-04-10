


def main():
    s = input().strip()
    t = input().strip()

    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1

    print(len(s) - i)


if __name__ == "__main__":
    main()