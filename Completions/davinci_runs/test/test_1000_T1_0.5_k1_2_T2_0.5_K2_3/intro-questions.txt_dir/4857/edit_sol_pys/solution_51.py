

import sys
import string

def main():
    L, W = map(int, sys.stdin.readline().split())

    if W > L * 26:  # 全て英小文字の文字列を作るときの最大の重さ
        print('impossible')
        return

    letters = string.ascii_lowercase
    weights = range(1, 27)
    letter_dict = dict(zip(letters, weights))  # 英小文字とその重さを対応付ける辞書

    for letter in letters:
        if W - letter_dict[letter] > 0:  # 重さを減らしていく
            print(letter, end='')
            W -= letter_dict[letter]
            L -= 1
        else:
            break

        if L == 1:
            print(letter)
            return

    while L > 0:  # 重さが0になった時点で、残りの文字は全てa
        print('a', end='')
        L -= 1

    print()

if __name__ == '__main__':
    main()
