
import sys

def main():
    n, a = map(int, sys.stdin.readline().split()) # a = 目標値, n = 個数
    e = list(map(int, sys.stdin.readline().split())) # e = リスト
    e.sort() # リストをソート
    e.reverse() # 逆順にソート
    count = 0
    for i in e: # リストを回す
        if a >= i: # 目標値がリストの値より大きいとき
            count += 1
            a -= i
    print(count)

if __name__ == '__main__':
    main()
