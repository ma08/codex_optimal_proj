
N, K, M = map(int, input().split())
A = list(map(int, input().split()))

sumA = sum(A)
avg = sumA / N

if avg >= M:
    print(0)  # 全員にM点以上取れるので、追加できる点数は0点
    exit()  # ここで終了

if K <= M:
    print(-1)  # 点数をK点以上追加することができないので、点数を追加することは不可能
    exit()  # ここで終了

print(M*N - sumA)  # ここまで来たら、点数を追加することは可能
