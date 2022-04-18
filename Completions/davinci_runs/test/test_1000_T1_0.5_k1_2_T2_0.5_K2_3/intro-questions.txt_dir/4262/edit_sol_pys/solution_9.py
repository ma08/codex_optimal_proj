'''
問題文
整数 N が与えられます。
整数 N が与えられたとき、N 個の整数を昇順に並べるために、入れ替える回数の最小値を求めてください。
制約
1≤ N ≤ 100
入力は全て整数である。
入力
入力は以下の形式で標準入力から与えられる。
N a1,a2,…,aN
'''


def swap(p, q):
    temp = p
    p = q
    q = temp
    return p, q


def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if A[i] > A[j]:
                A[i], A[j] = swap(A[i], A[j])
                count += 1

    print(count)


if __name__ == '__main__':
    main()
