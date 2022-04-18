def main():
    n = int(input())
    a, b, c = 0, 0, 0
    for i in range(n):
        s = input()
        if s[0] == 'B' and s[-1] == 'A':
            a += 1
        elif s[0] == 'B' and s[-1] == 'C':
            b += 1
        elif s[0] == 'C' and s[-1] == 'A':
            c += 1
    if a == 0 and b == 0 and c == 0:
        print(0)
        return


    if a == 0:
        a = 0
    else:
        a -= 1

    if b == 0:
        b = 0
    else:
        b -= 1

    if c == 0:
        c = 0
    else:
        c -= 1

    if a == 0 and b == 0 and c == 0:
        print(0)
        return
    ans = a + b + c + min(a, b, c)
    print(ans)


if __name__ == '__main__':
    main()
