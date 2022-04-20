

n, k = map(int, input().split())
a = list(map(int, input().split()))

# First, find the gcd of the array
gcd = a[0]
for i in range(1, n):
    gcd = math.gcd(gcd, a[i])

# Then, divide each element by the gcd, and count the number of times
# we can divide by 2.
# Since we can divide each element by 2 any number of times, we can
# divide the gcd by 2 as many times as needed.

# We do this by counting the number of 1s in the binary
# representation of the gcd.

# This is because the gcd is the product of the common prime factors
# of each element of the array.
# If we divide each element of the array by the gcd, we will have
# the remaining prime factors.
# The remaining prime factors of each element can be divided by 2 as
# many times as needed.
# Therefore, we can divide the gcd by 2 as many times as needed.

# We count the number of 1s in the binary representation of the gcd
# to find out how many times we can divide the gcd by 2.
count = 0
while gcd % 2 == 0:
    count += 1
    gcd //= 2

# Then, we find the minimum number of operations needed to get at
# least k equal numbers in the array.
# This is the number of operations needed to divide the gcd by 2
# (count) plus the number of operations needed to get at least k
# equal numbers in the array after dividing the gcd by 2.
min_operations = count + math.ceil(math.log(k, 2))

print(min_operations)