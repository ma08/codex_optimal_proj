

import math

N = int(input())

# This is the number of digits in N
digits = math.floor(math.log10(N)) + 1

# This is the sum of the digits in N
sum = 0
for i in range(0, digits):
    sum += (N // (10 ** i)) % 10

# If the number of digits is even and the sum of digits is odd, we can't reach N
if (digits % 2 == 0) and (sum % 2 == 1):
    print(-1)
    exit()

# We can reach (N, N) in N moves
if N <= 10 ** 5:
    print(N)
    exit()

# We can reach (N, N) in N - (10 ** 5) moves
if N <= 10 ** 10:
    print(N - (10 ** 5))
    exit()

# We can reach (N, N) in N - (10 ** 5) - (10 ** 5) moves
if N <= 10 ** 15:
    print(N - (10 ** 5) - (10 ** 5))
    exit()

# We can reach (N, N) in N - (10 ** 5) - (10 ** 5) - (10 ** 5) moves
if N <= 10 ** 20:
    print(N - (10 ** 5) - (10 ** 5) - (10 ** 5))
    exit()

# We can reach (N, N) in N - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) moves
if N <= 10 ** 25:
    print(N - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5))
    exit()

# We can reach (N, N) in N - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) moves
if N <= 10 ** 30:
    print(N - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5))
    exit()

# We can reach (N, N) in N - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) moves
if N <= 10 ** 35:
    print(N - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5))
    exit()

# We can reach (N, N) in N - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) moves
if N <= 10 ** 40:
    print(N - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5))
    exit()

# We can reach (N, N) in N - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) moves
if N <= 10 ** 45:
    print(N - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5))
    exit()

# We can reach (N, N) in N - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) moves
if N <= 10 ** 50:
    print(N - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5))
    exit()

# We can reach (N, N) in N - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) moves
if N <= 10 ** 55:
    print(N - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5))
    exit()

# We can reach (N, N) in N - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) moves
if N <= 10 ** 60:
    print(N - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5))
    exit()

# We can reach (N, N) in N - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) moves
if N <= 10 ** 65:
    print(N - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5))
    exit()

# We can reach (N, N) in N - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) moves
if N <= 10 ** 70:
    print(N - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5))
    exit()

# We can reach (N, N) in N - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) moves
if N <= 10 ** 75:
    print(N - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5))
    exit()

# We can reach (N, N) in N - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) moves
if N <= 10 ** 80:
    print(N - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5))
    exit()

# We can reach (N, N) in N - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) moves
if N <= 10 ** 85:
    print(N - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5))
    exit()

# We can reach (N, N) in N - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) moves
if N <= 10 ** 90:
    print(N - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5))
    exit()

# We can reach (N, N) in N - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) moves
if N <= 10 ** 95:
    print(N - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5))
    exit()

# We can reach (N, N) in N - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) moves
if N <= 10 ** 100:
    print(N - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5))
    exit()

# We can reach (N, N) in N - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) moves
if N <= 10 ** 105:
    print(N - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5))
    exit()

# We can reach (N, N) in N - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) moves
if N <= 10 ** 110:
    print(N - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5) - (10 ** 5))
    exit()