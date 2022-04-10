

N = int(input())
d = list(map(int, input().split()))

# dをソートして、それぞれの値がいくつあるか調べる
d.sort()
# 同じ値が複数ある場合は1つにまとめる
d_uniq = []
temp = d[0]
count = 1
for i in range(1, N):
    if d[i] == temp:
        count += 1
    else:
        d_uniq.append([temp, count])
        temp = d[i]
        count = 1
d_uniq.append([temp, count])

# 累積和を求める
d_uniq_sum = []
sum = 0
for i in range(len(d_uniq)):
    sum += d_uniq[i][1]
    d_uniq_sum.append([d_uniq[i][0], sum])

# 条件を満たすKの個数を求める
ans = 0
for i in range(len(d_uniq_sum)):
    if d_uniq_sum[i][1] == (N - d_uniq_sum[i][1]):
        ans += 1
print(ans)