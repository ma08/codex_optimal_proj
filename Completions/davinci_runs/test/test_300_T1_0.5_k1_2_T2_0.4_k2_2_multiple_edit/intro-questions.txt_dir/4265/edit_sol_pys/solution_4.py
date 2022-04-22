

import sys

def main():
    s = input()  # 入力文字列1
    t = input()  # 入力文字列2
    count = 0
    for i in range(len(s)):  # sとtの長さが同じなので、sの文字数分ループ
        if s[i] != t[i]:
            count += 1  # sとtで異なる文字がある場合、カウントを1つ増やす
    print(count)

if __name__ == '__main__':
    main()
