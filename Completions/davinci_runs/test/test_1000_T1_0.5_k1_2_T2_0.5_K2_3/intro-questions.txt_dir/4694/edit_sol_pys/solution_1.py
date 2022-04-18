

# input
N = int(input())
a_list = list(map(int, input().split()))

# initialization
a_list.sort()

# find the minimum distance
result = float('inf')
for i in range(1, N):
    result = min(result, a_list[i] - a_list[i-1])

# output
print(result)
