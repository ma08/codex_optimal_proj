# -*- coding: utf-8 -*-


def main():
    # 入力
    s = raw_input()
    t = raw_input()

    # 初期化
    count = 0

    # sとtの異なる文字数を数える
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1

    # 出力
    print '%d' % count

if __name__ == '__main__':
    main()
