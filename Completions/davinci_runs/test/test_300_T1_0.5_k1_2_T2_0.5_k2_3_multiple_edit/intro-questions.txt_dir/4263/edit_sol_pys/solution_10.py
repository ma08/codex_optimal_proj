# https://atcoder.jp/contests/abc088/tasks/abc088_b

import sys

def main():
    S = sys.stdin.readline().rstrip()
    max_len = 0
    curr_len = 0
    for c in S:
        if c == 'A' or c == 'C' or c == 'G' or c == 'T': # 小文字にするとWA
            curr_len += 1
        else:
            if curr_len > max_len:
                max_len = curr_len
            curr_len = 0
    if curr_len > max_len: # 最後の文字がACGTの場合にこの処理がないとWAになる
        max_len = curr_len
    print(max_len)

if __name__ == '__main__':
    main()
