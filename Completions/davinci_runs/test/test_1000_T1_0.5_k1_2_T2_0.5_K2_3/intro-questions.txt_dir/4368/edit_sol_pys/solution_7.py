
# get inputs
n, k = map(int, input().split())  # n: number, k: base

# initialize
digits = 0

# iterate until n is 0
while n > 0:
    # increment digit count
    digits += 1
    # divide by k
    n //= k

# print result
print(digits)
