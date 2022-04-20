

def main():
  S = input()
  T = input()
  s_len = len(S)
  t_len = len(T)
  dp = [[0 for _ in range(s_len+1)] for _ in range(t_len+1)]
  for i in range(1, t_len+1):
    for j in range(1, s_len+1):
      if T[i-1] == S[j-1]:
        dp[i][j] = dp[i-1][j-1] + 1
      else:
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
  print(t_len - dp[t_len][s_len])

if __name__ == "__main__":
  main()