

N, Q = map(int, input().split())
S = input()

# 累積和を作る
ac_count = [0] * (N + 1)
for i in range(N):
    if S[i:i + 2] == "AC":
        ac_count[i + 1] = ac_count[i] + 1
    else:
        ac_count[i + 1] = ac_count[i]

for _ in range(Q):
    l, r = map(int, input().split())
    print(ac_count[r - 1] - ac_count[l - 1])