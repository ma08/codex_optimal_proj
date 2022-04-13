

inp = input().split()
N = int(inp[0])
M = int(inp[1])
if N > M:
    print("Dr. Chaz needs " + str(N - M) + " more piece of chicken!")
else:
    print("Dr. Chaz will have " + str(M - N) + " piece of chicken left over!")
