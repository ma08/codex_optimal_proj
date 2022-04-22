# coding: utf-8

import sys

    '''
    文字列の差異を計算する
    '''
def main():
    s = input()
    t = input()
    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()
