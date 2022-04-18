# coding: utf-8


N, M = map(int, input().split())  # N: 桁数 M: 条件の数
for i in range(10 ** N):  # 桁数分だけ繰り返す
    if all(str(i).zfill(N)[s - 1] == str(c) for s, c in (map(int, input().split()) for _ in range(M))):  # 全ての条件を満たすか
        print(i)  # 満たすならその数字を出力
        exit()  # 終了
print(-1)  # 満たす数字がなければ-1を出力
