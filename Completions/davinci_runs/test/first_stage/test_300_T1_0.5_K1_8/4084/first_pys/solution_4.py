

n, a, b = map(int, input().split())

# If you can't understand the problem, think of this as a problem of counting the number of 1's in the binary representation of N-1.
# Let's define a function f(n) as the number of 1's in the binary representation of n.
# f(n) = floor(n/2) + n % 2
# This is because, in the binary representation, the first digit from the right is divided by 2 and the rest of the digits are shifted to the left.
# This can be proved by induction.
# Now, let's define a function g(n, k) as the number of 1's in the binary representation of n, when we consider only the first k digits from the right.
# g(n, k) = f(floor(n/2^k)) + n % 2^k
# This is because, in the binary representation, the first k digits from the right are divided by 2^k and the rest of the digits are shifted to the left.
# This can be proved by induction.
# Now, we can define the number of blue balls among the first N balls as f(N-1).
# Let's define a function h(n, k) as the number of blue balls among the first n balls, when we consider only the first k digits from the right.
# h(n, k) = h(floor(n/2^k), k-1) + (n % 2^k) * a + (floor(n/2^k) % 2) * b
# This is because, in the binary representation, the first k digits from the right are divided by 2^k and the rest of the digits are shifted to the left.
# And, the last digit is 0 if and only if the number of 1's in the binary representation is even, which means the number of blue balls is even.
# Therefore, we add b to the number of blue balls.
# This can be proved by induction.
# Now, we can calculate the number of blue balls among the first N balls by h(N-1, floor(log_2(N-1))).

def h(n, k):
    if k == 0:
        return n * a
    return h(n // 2, k - 1) + n % 2 ** k * a + (n // 2 % 2) * b

print(h(n - 1, len(bin(n - 1)) - 3))