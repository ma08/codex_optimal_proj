
from sys import stdin


def main():
    n = int(stdin.readline())
    s = stdin.readline()
    open_brackets = 0
    close_brackets = 0
    answer = 0
    for i in range(n):
        if s[i] == '(': 
            open_brackets += 1
        else:
            if open_brackets > 0:
                open_brackets -= 1
            else:
                close_brackets += 1
        if open_brackets + close_brackets == 0:
            answer += 1
    print(answer)


if __name__ == '__main__':
    main()
