

def main():
    """
    1. 문자열의 길이가 3n임을 이용해서 각 문자열이 몇번씩 나왔는지 세어본다.
    2. ab, ba 일 경우에는 둘 중 하나를 먼저 넣고 나머지를 다 넣는다.
    3. ab, aa 일 경우에는 이미 존재하는 ab를 이용해서 나머지를 넣는다.
    4. ab, bb 일 경우에는 이미 존재하는 ab를 이용해서 나머지를 넣는다.
    5. ab, cc 일 경우에는 이미 존재하는 ab를 이용해서 나머지를 넣는다.
    6. aa, aa 일 경우에는 둘 중 하나를 먼저 넣고 나머지를 다 넣는다.
    7. aa, bb 일 경우에는 이미 존재하는 aa를 이용해서 나머지를 넣는다.
    8. aa, cc 일 경우에는 이미 존재하는 aa를 이용해서 나머지를 넣는다.
    9. bb, bb 일 경우에는 둘 중 하나를 먼저 넣고 나머지를 다 넣는다.
    10. bb, cc 일 경우에는 이미 존재하는 bb를 이용해서 나머지를 넣는다.
    11. cc, cc 일 경우에는 둘 중 하나를 먼저 넣고 나머지를 다 넣는다.
    """
    n = int(input())
    s = input()
    t = input()

    if len(s) != 2 or len(t) != 2 or s[0] == t[0] or s[0] == t[1] or s[1] == t[0] or s[1] == t[1]:
        print("NO")
        return

    if s[0] == s[1]:
        if t[0] == t[1]:
            if s == t:
                print("YES")
                print((s[0]+s[1])*n)
            else:
                print("YES")
                print((s[0]+s[1])*n)
        else:
            print("YES")
            print((s[0]+t[0])*n+t[1]*n)
    elif t[0] == t[1]:
        print("YES")
        print((s[0]+s[1])*n+t[0]*n)
    elif s == t:
        print("YES")
        print((s[0]+s[1])*n)
    else:
        print("YES")
        print((s[0]+t[0])*n+t[1]*n)


if __name__ == "__main__":
    main()
