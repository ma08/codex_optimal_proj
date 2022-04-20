
# read input
N = int(input())
H = list(map(int, input().split()))

# count the number of moves
# the number of moves is the maximum number of consecutive steps where the height decreases.
count = 0
max_count = 0
for i in range(N-1):
    if H[i] >= H[i+1]:
        count += 1
    elif H[i] < H[i+1]:
        max_count = max(max_count, count)
        count = 0
max_count = max(max_count, count)

# output
print(max_count)
