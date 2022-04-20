
# Solution

a, n, m = map(int, input().split())

left = [0] * n
right = [0] * n

for i in range(n):
    left[i], right[i] = map(int, input().split())

x_list = [0] * m
p_list = [0] * m

for i in range(m):
    x_list[i], p_list[i] = map(int, input().split())

dp_list = [0] * (a + 1)

for i in range(a):
    dp_list[i + 1] = dp_list[i] + 1
    for j in range(m):
        if x_list[j] <= i:
            dp_list[i + 1] = min(dp_list[i + 1], dp_list[i] + p_list[j])

for i in range(n):
    if dp_list[left[i]] == dp_list[right[i]]:
        print(-1)
        exit()

print(dp[a])
