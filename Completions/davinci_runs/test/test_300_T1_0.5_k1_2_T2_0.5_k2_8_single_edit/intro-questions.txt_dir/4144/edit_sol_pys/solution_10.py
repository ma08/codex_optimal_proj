import sys
sys.setrecursionlimit(10 ** 6)
MOD = 10 ** 9 + 7


N = int(input())


# dp[i][j] : i桁目までで、jと同じ数字を書いたときの組み合わせ
# i桁目でjと同じ数字を書く場合は、
# i + 1桁目でjと同じ数字を書く場合と
# i + 1桁目でjと異なる数字を書く場合の2通り
# i桁目でjと異なる数字を書く場合は、
# i + 1桁目でjと異なる数字を書く場合の9通り
dp = [[0 for _ in range(10)] for _ in range(N + 1)]


for i in range(10):
    dp[1][i] = 1


print(solve())
