

from sys import stdin


def main():
    n = int(stdin.readline())
    s = stdin.readline()
    opened = 0
    closed = 0
    ans = 0
    for i in range(n):
        if s[i] == '(':
            opened += 1
        else:
            if opened > 0:
                opened -= 1
            else:
                closed += 1
        if opened + closed == 0:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()