
# input
N = int(input())
a_list = list(map(int, input().split()))  # a_list: list of int

# initialization
a_list.sort()

# find the minimum distance between a_list[i] and a_list[i-1]
result = float('inf')  # result: int
for i in range(1, N):
    result = min(result, a_list[i] - a_list[i-1])

# output
print(result)
