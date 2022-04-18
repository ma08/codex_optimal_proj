import sys

def main():
    S = sys.stdin.readline().rstrip()  # 文字列Sを取得
    max_len = 0
    curr_len = 0
    for c in S:  # 文字列Sの文字をすべて取り出す
        if c == 'A' or c == 'C' or c == 'G' or c == 'T':
            curr_len += 1  # 制限された文字であればカウントアップ
        else:
            if curr_len > max_len:
                max_len = curr_len
            curr_len = 0
    if curr_len > max_len:
        max_len = curr_len
    print(max_len)

if __name__ == '__main__':
    main()
