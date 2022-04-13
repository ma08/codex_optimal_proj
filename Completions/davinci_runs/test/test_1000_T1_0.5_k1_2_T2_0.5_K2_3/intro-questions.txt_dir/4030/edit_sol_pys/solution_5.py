

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
    if (s[0] == s[1]):
        print(1)
        print(1, 1, 1, 1, 1, 1, 1, 1)
        return
    

if __name__ == "__main__":
    main()
