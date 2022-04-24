# file
#


def main():
    s = input().strip()
    t = input().strip()

    if s == t:
        print("Yes")
        return

    if len(set(s)) != len(set(t)):
        print("No")
        return


    if len(s) != len(t):
        s = s + s

    for i in range(1, len(s)):
        if s[-i:] + s[:-i] == t:
            print('Yes')
            return 

    print("No")


if __name__ == '__main__':
    main()
