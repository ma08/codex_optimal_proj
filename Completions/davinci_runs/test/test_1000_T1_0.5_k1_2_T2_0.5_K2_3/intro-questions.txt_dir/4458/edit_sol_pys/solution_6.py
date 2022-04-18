
import sys

def main():
    input = sys.stdin.readline
    N = int(input())  # 入力値の取得
    P = [int(i) for i in input().split()]  # 入力値を配列として取得
    ans = 0
    for i in range(N):
        if P[i] == i + 1:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
