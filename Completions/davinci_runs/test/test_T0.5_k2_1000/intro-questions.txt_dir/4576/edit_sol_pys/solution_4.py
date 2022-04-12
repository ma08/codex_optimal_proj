
# get input
A = int(input())
B = int(input())
C = int(input())
X = int(input())

# initialize the number of ways
num_ways = 0

# loop over all combinations of the number of 500 yen coins A
for i in range(A + 1):
    # loop over all combinations of the number of 100 yen coins
    for j in range(B + 1):
        # loop over all combinations of the number of 50 yen coins
        for k in range(C + 1):
            # check if the total amount is X
            if (500 * i + 100 * j + 50 * k) == X:
                # increment the number of ways
                num_ways += 1

# print the number of ways
print(num_ways)
