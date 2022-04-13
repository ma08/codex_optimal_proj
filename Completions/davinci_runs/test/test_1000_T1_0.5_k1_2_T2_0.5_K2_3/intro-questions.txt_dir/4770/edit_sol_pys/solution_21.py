

inp = input().split()
N = int(inp[0])
M = int(inp[1])
if N > M:
    print("Dr. Chaz needs", N - M, "more pieces of chicken!")
else:
    print("Dr. Chaz will have", M - N, "pieces of chicken left over!")
