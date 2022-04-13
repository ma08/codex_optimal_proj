
# Input
N = int(input())
a_list = list(map(int, input().split()))

# Initialization
a_list.sort()

# Find the minimum distance
result = float('inf')
for i in range(1, N):
    result = min(result, a_list[i] - a_list[i-1])

# Output
print(result)
