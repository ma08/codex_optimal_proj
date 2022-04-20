

# SOLUTION
# The problem is to find the permutation of the array b that gives us the array a
# The permutation is as follows:
# 1. For every element in a, if it is prime, we add it to the end of the array
# 2. For every element in a, if it is composite, we add its largest factor to the end of the array
# 3. We shuffle the array
# We can see that the last element of the array b is always a prime
# We can also see that the last element of the array a is always a prime
# So, we can find the last element of the array a by finding the last element of the array b
# Then, the second last element of the array b is the largest factor of the second last element of the array a
# In general, for every element in the array b, we find the largest factor of the element before it in the array a
# We keep doing this until we reach the first element of the array a

# FUNCTION TO CHECK WHETHER A NUMBER IS PRIME OR NOT
def isPrime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

# FUNCTION TO FIND THE LARGEST FACTOR OF A NUMBER WHICH IS NOT EQUAL TO THE NUMBER
def findLargestFactor(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return n // i
        i += 1
    return 1

# GETTING THE INPUT
n = int(input())
b = list(map(int, input().split()))

# INITIALISING THE ARRAY a
a = [0] * n

# INITIALISING THE INDEXES
i = 0
j = n - 1

# FINDING THE FIRST ELEMENT OF THE ARRAY a
a[i] = b[j]

# FINDING THE SECOND ELEMENT OF THE ARRAY a
a[i + 1] = findLargestFactor(b[j - 1])

# FINDING THE REMAINING ELEMENTS OF THE ARRAY a
while i < n - 2:
    if isPrime(b[j - 2]):
        a[i + 2] = b[j - 2]
    else:
        a[i + 2] = findLargestFactor(b[j - 2])
    i += 1
    j -= 1

# PRINTING THE ARRAY a
print(*a)