
# get input
n, k = map(int, input().split())

# initialize
digits = 0

# iterate until n is 0
while n > 0:
    # increment digit count by 1
    digits += 1
    # divide by k
    n //= k

# print result
print(digits)
