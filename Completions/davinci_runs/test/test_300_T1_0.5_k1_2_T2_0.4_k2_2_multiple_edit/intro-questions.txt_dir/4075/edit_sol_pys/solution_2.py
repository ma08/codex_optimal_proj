
import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    bulbs = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
    states = list(map(int, sys.stdin.readline().split()))
    switches = [[False] * n for _ in range(m)] # m個のスイッチにおいて、n個の電球がついているかを表す
    for i in range(m): # スイッチiについて
        for j in range(1, bulbs[i][0] + 1): # スイッチiについている電球jについて
            switches[i][bulbs[i][j] - 1] = True # スイッチiについている電球jが、電球jについている
    cnt = 0
    for i in range(2 ** n): # 電球の状態を全探索
        flag = True # 電球の状態iが正しいか
        for j in range(m): # スイッチjについて
            c = 0
            for k in range(n):
                if switches[j][k] and ((i >> k) & 1):
                    c += 1
            if c % 2 != states[j]:
                flag = False
                break
        if flag:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()
