

import math

n = int(input())

if n <= 2:
    print(0)
    exit()

# n = 2*x + 2*y + 2*z + x*y + y*z + z*x
# n = 2*(x+y+z) + x*y + y*z + z*x
# n = 2*(x+y+z) + (x+y)(y+z)(z+x)
# n = 2*(x+y+z) + (x+y+z)(xy+yz+zx)
# We want to find (x+y+z) s.t. 2*(x+y+z) <= n and (x+y+z)(xy+yz+zx) <= n
# For each possible value of (x+y+z) we can find (xy+yz+zx) and check
# if that value is <= n.
# This is similar to the "sum of divisors" problem.

# We can make this faster by only looking at divisors of n.
# x+y+z has to divide n and xy+yz+zx has to divide n.
# If we look at all the divisors of n, we can check if there is a triple
# that satisfies the condition in O(1) time.

# For each divisor, we can find the number of ordered triples that add up to that divisor.
# To do this, we can use the "stars and bars" method.
# We have to find all the ways to split n stars into 3+1 bars.
# For each divisor, we can get the number of ways to split n stars into 3+1 bars in O(1) time.

# We can make this even faster by only looking at divisors of n that are less than or equal to sqrt(n).
# For each divisor, we can find a partner divisor that satisfies the condition in O(1) time.

divisors = [1]
for i in range(2, int(math.sqrt(n))+1):
    if n % i == 0:
        divisors.append(i)
        if i * i != n:
            divisors.append(n // i)

# n = n + (n-1) + (n-2) + ... + (n-(n-1)) = n * (n+1) / 2
# We can also find the number of ordered triples that add up to n in O(1) time.

num_triples = n * (n+1) // 2

for divisor in divisors:
    # We can find the number of ways to split n stars into 3+1 bars in O(1) time.
    num_triples -= n // divisor * (n // divisor + 1) // 2 * (n // divisor + 2) // 3
    # We can find the number of ways to split n stars into 3+1 bars in O(1) time.
    num_triples -= n // divisor * (n // divisor + 1) // 2 * (n // divisor + 2) // 3 * (n // divisor + 3) // 4

print(num_triples)
