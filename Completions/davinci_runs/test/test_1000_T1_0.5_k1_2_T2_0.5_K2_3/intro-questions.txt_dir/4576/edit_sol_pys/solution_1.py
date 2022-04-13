
# get input from the user
a = int(input())
b = int(input())
c = int(input())
x = int(input())

# initialize the number of ways
num_ways = 0

# loop over all combinations of the number of 500 yen coins
for i in range(a + 1):
    # loop over all combinations of the number of 100 yen coins
    for j in range(b + 1):
        # loop over all combinations of the number of 50 yen coins
        for k in range(c + 1):
            # check if the total amount is X
            if (500 * i + 100 * j + 50 * k) == x:
                # increment the number of ways
                num_ways += 1

# print the number of ways
print(num_ways)
# get input from the user
a = int(input())
b = int(input())
c = int(input())
x = int(input())

# initialize the number of ways
num_ways = 0

# loop over all combinations of the number of 500 yen coins
for i in range(a + 1):
    # loop over all combinations of the number of 100 yen coins
    for j in range(b + 1):
        # loop over all combinations of the number of 50 yen coins
        for k in range(c + 1):
            # check if the total amount is X
            if (500 * i + 100 * j + 50 * k) == x:
                # increment the number of ways
                num_ways += 1

# print the number of ways
print(num_ways)

# get input from the user
a = int(input())
b = int(input())
c = int(input())
x = int(input())

# initialize the number of ways
num_ways = 0

# loop over all combinations of the number of 500 yen coins
for i in range(a + 1):
    # loop over all combinations of the number of 100 yen coins
    for j in range(b + 1):
        # loop over all combinations of the number of 50 yen coins
        for k in range(c + 1):
            # check if the total amount is X
            if (500 * i + 100 * j + 50 * k) == x:
                # increment the number of ways
                num_ways += 1

# print the number of ways
print(num_ways)
