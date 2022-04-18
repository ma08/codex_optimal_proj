

# input
N = int(input())
a_list = list(map(int, input().split()))

# a_list.sort()

# find the minimum distance
# result = float('inf')
# for i in range(1, N):
#     result = min(result, a_list[i] - a_list[i-1])

# output
# print(result)

# input
N = int(input())
a_list = list(map(int, input().split()))

# initialization
# initialization
a_list.sort()

# find the minimum distance of the adjacent numbers
result = a_list[1] - a_list[0]
for i in range(2, N):
    result = min(result, a_list[i] - a_list[i - 1])

# output
print(result)
