

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
            print(1, 1)
        else:
            print(2)
            print(1, 2)
        return
    if (n == 3):
        if (s[0] < s[1] and s[1] < s[2]):
            print(1)
            print(1, 1, 1)
        elif (s[0] < s[1] and s[1] > s[2]):
            print(2)
            print(1, 2, 1)
        elif (s[0] > s[1] and s[1] < s[2]):
            print(2)
            print(2, 1, 1)
        else:
            print(3)
            print(1, 2, 3)
        return
    if (s[0] == 'a' and s[1] == 'a'):
        print(1)
        print(1, 1, 1, 1, 1, 1, 1, 1, 1)
        return
    if (s[0] == 'a' and s[1] == 'b'):
        print(1)
        print(1, 1, 1, 1, 1, 1, 1, 1)
        return
    if (s[1] == 'a' and s[2] == 'b'):
        print(1)
        print(2, 1, 1, 1, 1, 1, 1, 1)
        return
    if (s[2] == 'a' and s[3] == 'b'):
        print(1)
        print(2, 2, 1, 1, 1, 1, 1, 1)
        return
    if (s[3] == 'a' and s[4] == 'b'):
        print(1)
        print(2, 2, 2, 1, 1, 1, 1, 1)
        return
    if (s[4] == 'a' and s[5] == 'b'):
        print(1)
        print(2, 2, 2, 2, 1, 1, 1, 1)
        return
    if (s[5] == 'a' and s[6] == 'b'):
        print(1)
        print(2, 2, 2, 2, 2, 1, 1, 1)
        return
    if (s[6] == 'a' and s[7] == 'b'):
        print(1)
        print(2, 2, 2, 2, 2, 2, 1, 1)
        return
    if (s[7] == 'a' and s[8] == 'b'):
        print(1)
        print(2, 2, 2, 2, 2, 2, 2, 1)
        return
    print(2)
    print(1, 2, 1, 2, 1, 2, 1, 2, 1)
    return

if __name__ == "__main__":
    main()
