

n, m = map(int, input().split())
broken = set(map(int, [input() for _ in range(m)])) # 손상된 키수를 set으로 만들어준다. 

dp = [0] * (n+1) # dp 배열 선언
dp[0] = 1 # 초기값 설정
dp[1] = 1 # 초기값 설정

for i in range(2, n+1):
    if i in broken: # 손상된 키수가 있다면 이동할 수 없다.
        continue
    dp[i] = dp[i-1] + dp[i-2] # 현재 위치가 손상된 키수가 아니라면 이전에 있던 위치에서 온 경우의 수를 더해준다.

print(dp[n] % 1000000007)
