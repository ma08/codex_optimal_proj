
inp = input().split()
N = int(inp[0])
M = int(inp[1])
if N > M:
    print("Dr. Chaz needs", N - M, "more piece of chicken!")
else:
    print("Dr. Chaz will have", M - N, "piece of chicken left over!")
