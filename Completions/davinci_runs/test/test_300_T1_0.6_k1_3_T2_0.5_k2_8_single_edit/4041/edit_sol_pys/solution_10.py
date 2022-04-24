

# get the input
n, k, x, y = [int(x) for x in input().split()]

# define the answer
answer = 0

# if the number of houses is less than k
if n < k:
    # then the answer is the cost of the houses
    answer = n * x
# otherwise
else:
    # the answer is the cost of k houses, plus the cost of the rest
    answer = k * x + (n - k) * y

# output the answer (after converting to a string)
print(str(answer))
