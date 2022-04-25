
# n = int(input())
a = list(map(int, input().split()))  # a = [1, 2, 3, 4, 5]

# # find indices of all elements with value of 2
# indices = [i for i, x in enumerate(a) if x == 2]
# print(indices)


# find all elements with value of 2
a = [i for i in a if i == 2]
print(a)
