

# The point is to find the smallest possible absolute value of the coordinate of the destination.
# First, find the absolute value of (X - K * D). (A)
# Then, find the remainder of (A) / (2 * D).
# If the remainder is 0, the distance is (A) / 2.
# If the remainder is 1, the distance is (A) / 2 + 1.

X, K, D = map(int, input().split())

if X < 0:
    X = -X  # (A)

if X < K * D:
    K = K - (X + K * D) // (2 * D)  # (B)
    X = (X + K * D) % (2 * D)  # (C)

if X % (2 * D) == 0:
    print(X // (2 * D))
else:
    print(X // (2 * D) + 1)
