

def main():
    n = int(input())
    s = input()
    t = input()

    if n == 1:
        if s[0] == t[0]:
            print('YES')
            print('abc')
        elif s[0] == t[1]:
            print('YES')
            print('bac')
        elif s[1] == t[0]:
            print('YES')
            print('acb')
        elif s[1] == t[1]:
            print('YES')
            print('cab')
        else:
            print('NO')
    elif n == 2:
        if s[0] == t[0] or s[1] == t[1]:
            print('NO')
        elif s[0] == t[1]:
            print('YES')
            print('bac' + s[1] + t[0] + 'bac')
        elif s[1] == t[0]:
            print('YES')
            print('acb' + s[0] + t[1] + 'acb')
        else:
            print('YES')
            print(s[0] + t[1] + s[1] + t[0] + s[0] + t[1] + s[1] + t[0])
    else:
        if s[0] == t[0] or s[1] == t[1]:
            print('NO')
        elif s[0] == t[1]:
            print('YES')
            print('bac'*n + s[1] + t[0] + 'bac'*n)
        elif s[1] == t[0]:
            print('YES')
            print('acb'*n + s[0] + t[1] + 'acb'*n)
        else:
            print('YES')
            print(s[0] + t[1] + s[1] + t[0]*(n-1) + s[0] + t[1] + s[1] + t[0]*(n-1))


if __name__ == "__main__":
    main()