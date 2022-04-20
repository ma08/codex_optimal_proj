

# SOLUTION

import sys

def main():
    a, n, m = map(int, sys.stdin.readline().split())
    rain = [0] * (a + 1)
    for i in range(n):
        l, r = map(int, sys.stdin.readline().split())
        rain[l] += 1
        rain[r] -= 1
    for i in range(a):
        rain[i + 1] += rain[i]
    umbrellas = []
    for i in range(m):
        x, p = map(int, sys.stdin.readline().split())
        umbrellas.append((x, p))
    umbrellas.sort()
    dp = [0] * (a + 1)
    umbrellas.append((a + 1, 0))
    for i in range(a + 1):
        dp[i] = (1 << 30)
        if rain[i] == 0:
            continue
        for j in range(m + 1):
            if umbrellas[j][0] > i:
                break
            dp[i] = min(dp[i], dp[max(0, umbrellas[j][0] - 1)] + umbrellas[j][1])
    if dp[a] >= (1 << 30):
        print(-1)
    else:
        print(dp[a])

threading.Thread(target=main).start()