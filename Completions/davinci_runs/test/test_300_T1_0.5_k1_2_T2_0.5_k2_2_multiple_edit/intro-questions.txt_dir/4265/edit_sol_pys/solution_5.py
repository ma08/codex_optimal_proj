# -*- coding: utf-8 -*-


from collections import Counter


def main():
    n = int(input())
    s = input()
    t = input()

    ans = 0
    for i in range(n):
        if s[i] != t[i]:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
