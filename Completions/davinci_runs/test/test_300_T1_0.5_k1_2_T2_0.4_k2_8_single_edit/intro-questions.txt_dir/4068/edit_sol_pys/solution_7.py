
n, m = map(int, input().split())
broken = set(map(int, [input() for _ in range(m)]))  # 입력받은 것을 숫자로 변환하고, set으로 중복을 제거한다.

dp = [0] * (n+1)
dp[0] = 1  # 0은 1가지 방법이 있다.
dp[1] = 1  # 1은 1가지 방법이 있다.

for i in range(2, n+1):
    if i in broken:  # 버튼이 망가져 있다면
        continue  # 다음 버튼으로 넘어간다.
    dp[i] = dp[i-1] + dp[i-2]  # 망가지지 않았다면, 마지막 버튼을 누른 경우와 안누른 경우의 합이다.

print(dp[n] % 1000000007)
