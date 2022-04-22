


def main():
    s = input()
    t = input()

    ans = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()

s = input()
t = input()
