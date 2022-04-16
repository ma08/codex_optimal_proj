# -*- coding: utf-8 -*-

import sys

def print_diff_table(n, v):
    diff_table = [v[:]]
    while len(diff_table[-1]) > 1: # 差分表の最後の行の要素数が1より大きい間
        diff_table.append([]) # 新しい行を追加
        for i in range(len(diff_table[-2]) - 1): # 差分表の最後の行の要素数-1回繰り返す
            diff_table[-1].append(diff_table[-2][i + 1] - diff_table[-2][i]) # 差分を追加
    for i in range(len(diff_table)): # 差分表の行数分繰り返す
        print("\t".join(map(str, diff_table[i]))) # 差分表を出力
    print()

def main():
    n = int(sys.stdin.readline().strip())
    v = list(map(int, sys.stdin.readline().strip().split()))
    print_diff_table(n, v)

if __name__ == '__main__':
    main()
