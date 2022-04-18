

# The point is to find the smallest possible absolute value of the coordinate of the destination. First, find the absolute value of (X - K * D). Then, find the remainder of (X - K * D) / (2 * D). If the remainder is 0, the distance is (X - K * D) / 2. If the remainder is 1, the distance is (X - K * D) / 2 + 1.

X, K, D = map(int, input().split())  # Get input

if X < 0:
    X = -X  # If X is negative, make it positive

if X < K * D:
    K = K - (X + K * D) // (2 * D)  # If X is smaller than K * D, subtract the number of jumps needed to make it bigger
    X = (X + K * D) % (2 * D)  # Find the remainder of (X - K * D) / (2 * D)

if X % (2 * D) == 0:  # If the remainder is 0, the number of jumps is (X - K * D) / 2.
    print(X // (2 * D))  # Print the number of jumps
else:
    print(X // (2 * D) + 1)
