

def main():
    n = int(input())
    s = input()
    t = input()

    if len(s) != 2 or len(t) != 2:
        print("NO")
        return

    if s[0] == s[1]:
        if t[0] == t[1]:
            if s == t:
                print("YES")
                print(s[0]*n+s[1]*n+t[0]*n)
            else:
                print("YES")
                print(s[0]*n+s[1]*n+t[0]*n)
        else:
            print("YES")
            print(s[0]*n+t[0]*n+t[1]*n)
    elif t[0] == t[1]:
        print("YES")
        print(s[0]*n+s[1]*n+t[0]*n)
    elif s == t:
        print("YES")
        print(s[0]*n+s[1]*n+t[0]*n)
    else:
        print("YES")
        print(s[0]*n+t[0]*n+t[1]*n)


if __name__ == "__main__":
    main()
