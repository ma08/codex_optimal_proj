

import sys
sys.setrecursionlimit(10**6)

n = int(input())
s = input()

# Dynamic Programming
# dp[i][j] = number of ways to fill in brackets for a sequence of length i, ending with j ')'s
# dp[i][j] = sum_{k=0}^{j-1} dp[i-1][k]
# Base case: dp[0][0] = 1
#
# Final answer is sum_{j=1}^n dp[2n][j]
#
# dp[i][j] = sum_{k=0}^{j-1} dp[i-1][k]
#          = sum_{k=0}^{j-1} dp[i-2][k] + dp[i-2][k-1]
#          = sum_{k=0}^{j-1} dp[i-2][k] + dp[i-2][k]
#          = 2 * sum_{k=0}^{j-1} dp[i-2][k]
#          = 2 * dp[i-2][j-1]

dp = []
for i in range(n*2+1):
    dp.append([0]*(n+1))
dp[0][0] = 1
for i in range(2, n*2+1):
    for j in range(1, n+1):
        dp[i][j] = 2 * dp[i-2][j-1]

# print(dp)
# print(sum(dp[2*n]))

# Brute-force
# Create all possible sequences of length 2n
# Check if the given sequence is a substring
# Count the number of valid sequences
#
# Time limit exceeded

def check_validity(x):
    # Check if x is a valid sequence
    balance = 0
    for c in x:
        if c == '(':
            balance += 1
        elif c == ')':
            balance -= 1
        else:
            print("Error!")
        if balance < 0:
            return False
    if balance == 0:
        return True
    else:
        return False

def generate_all_sequences(n, x, i):
    if i == 2*n:
        if x in s:
            if check_validity(x):
                global num_valid_sequences
                num_valid_sequences += 1
    else:
        generate_all_sequences(n, x+'(', i+1)
        generate_all_sequences(n, x+')', i+1)

num_valid_sequences = 0
generate_all_sequences(n, '', 0)
print(num_valid_sequences)