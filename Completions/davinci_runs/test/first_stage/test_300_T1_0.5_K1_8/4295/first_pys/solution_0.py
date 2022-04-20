

# Process
# 1. Input N and K
# 2. If N % K == 0 -> N = N - K
# 3. Else -> N = N % K

# 1. Input N and K
N, K = map(int, input().split())

# 2. If N % K == 0 -> N = N - K
if N % K == 0:
    N = N - K

# 3. Else -> N = N % K
else:
    N = N % K

# 4. Output N
print(N)