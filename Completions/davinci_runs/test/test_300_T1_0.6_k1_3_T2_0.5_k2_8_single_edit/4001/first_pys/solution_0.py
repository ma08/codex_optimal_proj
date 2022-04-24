

n = int(input())
divisors = [int(x) for x in input().split()]

# Find all the divisors of the number that is the product of all the divisors.
# Those divisors will be the divisors for either x or y.
product = 1
for d in divisors:
    product *= d

# Find the divisors for the number that is the product of all the divisors.
# We will use the divisors as the possible divisors for x and y.
possible_divisors = []
for i in range(1, int(product ** 0.5) + 1):
    if product % i == 0:
        possible_divisors.append(i)
        possible_divisors.append(int(product / i))
possible_divisors = sorted(possible_divisors)

# We need to find the divisors for x and y.
# We will create a set of the possible divisors for x and y and then
# remove the divisors from the list when we find them.
#
# We will assume that the first divisor in the list is the largest divisor.
# We will just work our way backwards from the largest divisor and try
# to find a match.
possible_divisors = set(possible_divisors)
divisors_for_x = [divisors[0]]
possible_divisors.remove(divisors[0])

for d in divisors[1:]:

    # We will assume that the divisor is in the list of x.
    # We will try to find a match. If we find a match, then we
    # will remove the divisor from the list of possible divisors
    # for y and mark that divisor as a divisor for x.
    # If we don't find a match, then we will remove the divisor
    # from the list of possible divisors for x and mark that
    # divisor as a divisor for y.
    if d in possible_divisors:
        possible_divisors.remove(d)
        divisors_for_x.append(d)
    else:
        possible_divisors.remove(product // d)

# The remaining possible divisors are the divisors for y.
divisors_for_y = [d for d in possible_divisors]

# Calculate the product of the divisors for x and y.
x = 1
y = 1
for d in divisors_for_x:
    x *= d
for d in divisors_for_y:
    y *= d

print(x, y)