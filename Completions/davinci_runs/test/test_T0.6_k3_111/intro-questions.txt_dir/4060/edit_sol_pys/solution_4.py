
from sys import stdin


def main():
    n = int(stdin.readline())
    s = stdin.readline()
    open_brackets = 0
    closed_brackets = 0
    ans = 0
    for i in range(n):
        if s[i] == '(':
            open_brackets += 1
        else:
            if open_brackets > 0:
                open_brackets -= 1
            else:
                closed_brackets += 1
        if open_brackets + closed_brackets == 0:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
