# coding: utf-8
N, K = map(int, input().split())
D = set(map(int, input().split()))

for i in range(N, 10000):
    if all(d not in str(i) for d in D):  # 全ての条件を満たしているか
        print(i)
        break
