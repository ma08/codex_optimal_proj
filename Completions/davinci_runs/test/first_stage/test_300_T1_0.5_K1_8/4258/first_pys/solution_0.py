

# Get Input
A, B, T = map(int, input().split())

# Solve
# Biscuits produced after T seconds
T_Biscuits = (T // A) * B
# Biscuits produced within 0.5 seconds after T
if (T % A) > 0.5:
    T_Biscuits += B

# Output
print(T_Biscuits)