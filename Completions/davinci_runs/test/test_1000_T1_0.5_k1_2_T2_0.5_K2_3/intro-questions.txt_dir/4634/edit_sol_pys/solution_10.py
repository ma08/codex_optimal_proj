
# SOLUTION
# Step 1: find the start and end of the first contiguous subarray
# Step 2: count the number of 0s between the start and end of the first contiguous subarray
# Step 3: find the start and end of the next contiguous subarray
# Step 4: count the number of 0s between the end of the first contiguous subarray and the start of the next contiguous subarray
# Step 5: repeat until all contiguous segments are found

def minimumMoves(n, a):
    moves = 0
    start = 0
    end = 0
    for i in range(n):
        if a[i] == 1:
            end = i
            break

    for i in range(end+1, n):
        if a[i] == 1:
            moves += (i - end - 1)
            end = i
    return moves


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(minimumMoves(n, a))
