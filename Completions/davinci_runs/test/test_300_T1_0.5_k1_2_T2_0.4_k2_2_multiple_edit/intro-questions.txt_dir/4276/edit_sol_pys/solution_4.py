
import sys

def main():
    n, t = map(int, sys.stdin.readline().split())
    min_cost = t + 1  # 初期値を最大値にする
    for _ in range(n):
        cost, time = map(int, sys.stdin.readline().split())
        if time <= t:
            min_cost = min(min_cost, cost)
    if min_cost > t:  # 全てのコンピュータが条件を満たさない場合
        print("TLE")
    else:
        print(min_cost)

if __name__ == "__main__":
    main()
