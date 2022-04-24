# file
#


def main():
    s, t = input().split()

    if s == t:
        print("Yes")
        return

    if len(s) != len(t):
        print("No")
        return

    for i in range(len(s)):
        if s == t:
            print("Yes")
            return
        else:
            s = s[-1] + s[:-1]

    print("No")


if __name__ == '__main__':
    main()
