import sys

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    s = [i[0] for i in s if i[0] in ['M', 'A', 'R', 'C', 'H']]  # 先頭文字を取得
    s = list(set(s))  # 重複を削除
    print(len(s) * (len(s) - 1) * (len(s) - 2) // 6)  # 順列を計算

if __name__ == '__main__':
    main()
