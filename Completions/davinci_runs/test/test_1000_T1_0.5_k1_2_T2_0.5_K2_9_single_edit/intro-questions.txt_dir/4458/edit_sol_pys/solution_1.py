

import sys

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    P = [int(i) for i in input().split()] # 入力
    ans = 0
    for i in range(0, N):
        if P[i] == i + 1: # 正しい順番なら
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
