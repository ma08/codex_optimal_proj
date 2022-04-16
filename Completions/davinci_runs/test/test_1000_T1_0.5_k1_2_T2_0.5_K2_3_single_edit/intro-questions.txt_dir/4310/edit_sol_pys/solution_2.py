

# get input
A1, A2, A3 = map(int, input().split())

# calculate
ans = min(abs(A2 - A1) + abs(A3 - A2), abs(A3 - A1) + abs(A2 - A3), abs(A2 - A3) + abs(A1 - A2))

# output
print(ans)
