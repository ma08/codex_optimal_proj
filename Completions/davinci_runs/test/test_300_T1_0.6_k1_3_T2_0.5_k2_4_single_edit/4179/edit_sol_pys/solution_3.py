
import sys

def main():
    n, m, c = map(int, sys.stdin.readline().split())  # 入力
    b = list(map(int, sys.stdin.readline().split()))
    a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]  # 入力
    count = 0  # 答え
    for i in range(n):
        total = 0  # 合計
        for j in range(m):
            total += a[i][j] * b[j]  # 合計
        if total + c > 0:  # 合計 + C
            count += 1
    print(count)

if __name__ == '__main__':
    main()
