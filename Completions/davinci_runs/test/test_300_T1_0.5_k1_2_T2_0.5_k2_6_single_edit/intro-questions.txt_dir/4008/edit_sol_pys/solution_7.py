
# -*- coding: utf-8 -*-

def main():
    n = int(input())
    s = input()
    d = []
    for i in range(n):
        if s[i] == 'B':
            d.append(i)
    print(len(d))
    for i in range(len(d)):
        if i != len(d) - 1:
            print(d[i + 1] - d[i], end=' ')
        else:
            print(n - 1 - d[i])


if __name__ == '__main__':
    main()
