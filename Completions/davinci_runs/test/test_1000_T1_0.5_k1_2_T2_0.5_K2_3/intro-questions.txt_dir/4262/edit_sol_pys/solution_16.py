'''
問題文
整数Nが与えられます。
整数Nが与えられたとき、N個の整数を昇順に並べるために、入れ替える回数の最小値を求めてください。
制約
1≤N≤100
入力は全て整数である。
入力
入力は以下の形式で標準入力から与えられる。
N
a1,a2,…,aN
'''


def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if P[i] > P[j]:
                P[i], P[j] = P[j], P[i]
                count += 1
            if Q[i] > Q[j]:
                Q[i], Q[j] = Q[j], Q[i]
                count += 1
    print(count)


if __name__ == '__main__':
    main()
