
import sys

def main():
    n, m = map(int, input().split())
    switches = [list(map(int, input().split())) for _ in range(m)]
    states = list(map(int, input().split()))
    bulbs = [[False] * n for _ in range(m)]  # n行m列
    for i in range(m):
        for j in range(1, switches[i][0] + 1):
            bulbs[i][switches[i][j] - 1] = True
    # print(bulbs)
    cnt = 0  # 计数器
    for i in range(2 ** n):
        flag = True  # 判断是否满足条件
        for j in range(m):
            c = 0
            for k in range(n):
                if bulbs[j][k] and ((i >> k) & 1):  # 判断第k位是否为1
                    c += 1
            if c % 2 != states[j]:  # 判断是否满足第j个灯泡的状态
                flag = False
                break
        if flag:
            cnt += 1  # 满足条件的情况数
    print(cnt)

if __name__ == '__main__':
    main()
