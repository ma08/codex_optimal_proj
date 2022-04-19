

def main():
    n = int(input())
    s = input()
    if (n == 1):
        print(1)
        print(1)
        return
    if (n == 2):
        if (s[0] < s[1]):
            print(1)
            print(1, 1, sep=' ')
        else:
            print(2)
            print(1, 2, sep=' ')
        return
    if (n == 3):
        if (s[0] < s[1] and s[1] < s[2]):
            print(1)
            print(1, 1, 1, sep=' ')
        elif (s[0] < s[1] and s[1] > s[2]):
            print(2)
            print(1, 2, 1, sep=' ')
        elif (s[0] > s[1] and s[1] < s[2]):
            print(2)
            print(2, 1, 1, sep=' ')
        else:
            print(3)
            print(1, 2, 3, sep=' ')
        return
    if (s[0] == s[1]):
        print(1)
        print(1, 1, 1, 1, 1, 1, 1, 1, 1, sep=' ')
        return
    if (s[0] < s[1]):
        print(1)
        print(1, 1, 1, 1, 1, 1, 1, 1, sep=' ')
        return
    if (s[1] < s[2]):
        print(1)
        print(2, 1, 1, 1, 1, 1, 1, 1, sep=' ')
        return
    if (s[2] < s[3]):
        print(1)
        print(2, 2, 1, 1, 1, 1, 1, 1, sep=' ')
        return
    if (s[3] < s[4]):
        print(1)
        print(2, 2, 2, 1, 1, 1, 1, 1, sep=' ')
        return
    if (s[4] < s[5]):
        print(1)
        print(2, 2, 2, 2, 1, 1, 1, 1, sep=' ')
        return
    if (s[5] < s[6]):
        print(1)
        print(2, 2, 2, 2, 2, 1, 1, 1, sep=' ')
        return
    if (s[6] < s[7]):
        print(1)
        print(2, 2, 2, 2, 2, 2, 1, 1, sep=' ')
        return
    if (s[7] < s[8]):
        print(1)
        print(2, 2, 2, 2, 2, 2, 2, 1, sep=' ')
        return
    print(2)
    print(1, 2, 1, 2, 1, 2, 1, 2, 1, sep=' ')
    return

if __name__ == "__main__":
    main()
