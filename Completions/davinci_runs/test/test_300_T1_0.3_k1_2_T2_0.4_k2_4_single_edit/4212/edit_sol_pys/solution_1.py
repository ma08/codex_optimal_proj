
import sys

def main():
    n, m, q = map(int, sys.stdin.readline().split())
    a = [0] * (n + 1) # 配列の初期化
    for _ in range(q):
        ai, bi, ci, di = map(int, sys.stdin.readline().split())
        a[ai] += di # ai番目にdiを足す
        a[bi] -= di # bi番目からdiを引く
    for i in range(1, n + 1): # a[i]にa[i-1]を足す
        a[i] += a[i - 1] # これでa[i]にはi番目までの合計が入る
    print(max(a)) # 最大値を出力

if __name__ == '__main__':
    main()
