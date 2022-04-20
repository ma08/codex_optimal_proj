

import sys

def main():
    # Read input from stdin
    a = [list(map(int, input().split())) for _ in range(3)] # 入力を3行読み込む
    n = int(input())
    b = [int(input()) for _ in range(n)] # n行読み込む

    # Check if there is a bingo
    bingo = False
    for i in range(3): # 3行読み込む
        if bingo:
            break
        for j in range(3): # 3列読み込む
            if a[i][j] in b:
                bingo = True
                break
    if not bingo: # 横のチェック
        for i in range(3):
            if bingo:
                break
            for j in range(3):
                if a[j][i] in b:
                    bingo = True
                    break
    if not bingo: # 斜めのチェック
        for i in range(3):
            if a[i][i] in b:
                bingo = True
                break
    if not bingo:
        for i in range(3):
            if a[i][2-i] in b:
                bingo = True
                break

    # Print the result
    print('Yes' if bingo else 'No')

if __name__ == '__main__':
    main()
