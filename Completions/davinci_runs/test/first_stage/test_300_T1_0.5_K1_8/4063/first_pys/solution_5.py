

# N
n = int(input())

# d_1, d_2, ..., d_N
d = list(map(int, input().split()))

# sort d in ascending order
d.sort()

# number of choices of K
ans = 0

# loop through all possible values of K
for k in range(1, d[-1]):
    # number of problems for ARCs
    arcs = 0
    # number of problems for ABCs
    abcs = 0
    # loop through all problems
    for i in range(n):
        # if the difficulty of the problem is K or higher
        if d[i] >= k:
            # the problem is for ARCs
            arcs += 1
        # otherwise
        else:
            # the problem is for ABCs
            abcs += 1
    # if the number of problems for ARCs is equal to the number of problems for ABCs
    if arcs == abcs:
        # increment ans
        ans += 1

# print ans
print(ans)