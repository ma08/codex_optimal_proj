

# Get input
N = int(input())
A = list(map(int, input().split()))

# Find the maximum possible greatest common divisor of the N integers on the blackboard after your move.
# If the greatest common divisor of A_1, A_2, ..., A_N is x, then the maximum possible greatest common divisor of the N integers on the blackboard after your move is x.
# Therefore, we print the greatest common divisor of A_1, A_2, ..., A_N.
# The greatest common divisor of A_1, A_2, ..., A_N can be calculated using the following formula:
#   Let x be the greatest common divisor of A_1, A_2, ..., A_N
#   x = gcd(A_1, A_2, ..., A_N)
#   x = gcd(gcd(A_1, A_2), A_3, ..., A_N)
#   x = gcd(gcd(gcd(A_1, A_2), A_3), A_4, ..., A_N)
#   ...
#   x = gcd(gcd(gcd(..., A_{N-1}), A_N))
#
# The greatest common divisor of two integers a and b can be calculated using the Euclidean algorithm:
#   Let x be the greatest common divisor of a and b
#   x = gcd(a, b)
#   x = gcd(a, b % a)
#   x = gcd(b % a, a % (b % a))
#   ...
#   x = gcd(a % b, b % (a % b))
#   x = gcd(a % b, 0)
#   x = a % b
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(A[0], gcd(A[1], gcd(A[2], A[3]))))