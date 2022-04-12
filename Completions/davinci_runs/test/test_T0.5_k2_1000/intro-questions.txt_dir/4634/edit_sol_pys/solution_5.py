

# SOLUTION:
# Step 1: find the start and end of the first contiguous segment
# Step 2: count the number of 0s between the start and end of the first contiguous segment
# Step 3: find the start and end of the next contiguous segment
# Step 4: count the number of 0s between the end of the first contiguous segment and the start of the next contiguous segment
# Step 5: repeat until all contiguous segments are found

def minimum_moves(n, a):
    moves, start, end = 0, 0, 0
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
    print(minimum_moves(n, a))
