

# number of elements
n = int(input())

# permutation
p = list(map(int, input().split()))

# number of elements that satisfy the condition
count = 0

# check all elements
for i in range(1, n - 1):
    # check if the element is the second smallest among the three numbers
    if p[i - 1] < p[i] and p[i] < p[i + 1] or p[i - 1] > p[i] and p[i] > p[i + 1]:
        count += 1

# print the result
print(count)