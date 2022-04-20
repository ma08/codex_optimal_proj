
# Solution

a, n, m = map(int, input().split())  # a: 길이, n: 질문 개수, m: 지도 개수

l = [0] * n  # 질문 시작 지점
r = [0] * n  # 질문 끝 지점

for i in range(n):
    l[i], r[i] = map(int, input().split())

x = [0] * m  # 지도 시작 지점
p = [0] * m  # 지도 끝 지점

for i in range(m):
    x[i], p[i] = map(int, input().split())

dp = [0] * (a + 1)  # dp[i]: i까지 가는데 필요한 최소 비용

for i in range(a):
    dp[i + 1] = dp[i] + 1  # 길이가 1인 지도를 사용하는 경우
    for j in range(m):
        if x[j] <= i:
            dp[i + 1] = min(dp[i + 1], dp[i] + p[j])  # 지도를 사용하는 경우

for i in range(n):
    if dp[l[i]] == dp[r[i]]:  # 질문에 대한 답이 없는 경우
        print(-1)
        exit()

print(dp[a])
