
import sys

def main():
    n,m,c = map(int, input().split())
    b = list(map(int, input().split()))
    a = [list(map(int, input().split())) for i in range(n)]
    count = 0
    for i in range(n):  # n行
        if sum(a[i][j]*b[j] for j in range(m))+c > 0:  # m列
            count += 1  # 判定された回数をcountに加える
    print(count)  # countを出力


if __name__ == "__main__":
    main()  # main()関数を実行
