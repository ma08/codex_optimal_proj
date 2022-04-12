
import sys

def main():
    n, m, c = map(int, sys.stdin.readline().split()) # n: 機種数 m: パラメータ数 c: 判定基準
    b = list(map(int, sys.stdin.readline().split())) # パラメータ
    a = [list(map(int, sys.stdin.readline().split())) for i in range(n)] # 機種ごとのパラメータ
    count = 0
    for i in range(n):
        if sum(a[i][j]*b[j] for j in range(m)) + c > 0:
            count += 1
    print(count)

if __name__ == "__main__":
    main()
