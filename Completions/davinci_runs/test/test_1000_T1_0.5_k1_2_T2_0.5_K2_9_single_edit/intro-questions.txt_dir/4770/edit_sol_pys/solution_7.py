
inp = input().split()
N = int(inp[0])
M = int(inp[1])
if N > M:
    print("Dr. Chaz will have", N - M, "piece[s] of chicken left over!")
else:
    print("Dr. Chaz will have", M - N, "piece[s] of chicken left over!")
