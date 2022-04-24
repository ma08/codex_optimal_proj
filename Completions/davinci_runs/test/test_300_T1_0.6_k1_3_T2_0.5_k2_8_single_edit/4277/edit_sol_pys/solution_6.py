# -*- coding: utf-8 -*-


def main():
    n, a, b = map(int, input().split())

    if b / n >= a:
        print(a * n)
    elif a * n > b:
        print(b)
    else:
        print(-1)

if __name__ == '__main__':
    main()
