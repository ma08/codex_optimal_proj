


def main():
    n = int(input())
    s = [input() for _ in range(n)]
    m = 0
    a = 0
    r = 0
    c = 0
    h = 0
    for i in range(n):
        if s[i][0] == 'M':
            m += 1
        elif s[i][0] == 'A':
            a += 1
        elif s[i][0] == 'R':
            r += 1
        elif s[i][0] == 'C':
            c += 1
        elif s[i][0] == 'H':
            h += 1
    print(m*a*r + m*a*c + m*a*h + m*r*c + m*r*h + m*c*h + a*r*c + a*r*h + a*c*h + r*c*h)


if __name__ == '__main__':
    main()