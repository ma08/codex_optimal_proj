
N, K = map(int, input().split()) # N: 数字の桁数, K: 許容する数字の最大値
D = set(map(int, input().split())) # 許容しない数字

# print(N, K, D)

for i in range(N, 10000):
    if all(d not in str(i) for d in D):
        print(i)
        break
