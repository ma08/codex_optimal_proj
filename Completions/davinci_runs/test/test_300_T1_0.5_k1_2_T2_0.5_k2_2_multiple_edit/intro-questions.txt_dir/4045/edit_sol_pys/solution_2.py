

def main():
    n = int(input())
    s = input()
    t = input()

    if len(s) != 3 or len(t) != 3:
        print("NO")
        return

        return

    if s[0] == s[1] and s[1] == s[2]:
        if t[0] == t[1] and t[1] == t[2]:
            print("YES")
            print(s[0]*n)
            return
        else:
            print("YES")
            print(s[0]*n)
            return
    elif s[0] == s[1]:
        if t[0] == t[1] and t[1] == t[2]:
            print("YES")
            print(s[0]*n+s[2]*n)
            return
        elif t[0] == t[1]:
            print("YES")
            print(s[0]*n+s[2]*n)
            return
        else:
            print("YES")
            return
    elif t[0] == t[1] and t[1] == t[2]:
        print("YES")
        return
    elif t[0] == t[1]:
        print("YES")
        print(s[0]*n+s[2]*n)
        return
    else:
        print("YES")
        print(s[0]*n+t[0]*n+t[1]*n)


if __name__ == "__main__":
    main()
