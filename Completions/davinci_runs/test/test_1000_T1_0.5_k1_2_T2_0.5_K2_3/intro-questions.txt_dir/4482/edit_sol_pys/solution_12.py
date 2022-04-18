

N = int(input())
a = list(map(int, input().split()))

# 方針: 平均を取って、それらとの差を計算していく
average = sum(a) / len(a)

# 平均との差を計算し、２乗したものを足していく
diff_total = 0
for i in range(N):
    diff_total += (a[i] - average) ** 2



print(int(diff_total))
