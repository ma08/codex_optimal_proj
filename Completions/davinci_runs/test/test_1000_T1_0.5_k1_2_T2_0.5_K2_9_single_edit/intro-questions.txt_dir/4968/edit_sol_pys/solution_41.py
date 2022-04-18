# Get input
N, M = [int(x) for x in input().split()]
L = [int(x) for x in input().split()]


# Find the number of teams that can start
canStart = 0
for i in range(N):
    if i == 0:
        if L[i] == 1 or L[i + 1] == 1:
            canStart += 1
    elif i == N - 1:
        if L[i] == 1 or L[i - 1] == 1:
            canStart += 1
    else:
        if L[i] == 1 or L[i - 1] == 1 or L[i + 1] == 1:
            canStart += 1

# Print the result
print(canStart)
