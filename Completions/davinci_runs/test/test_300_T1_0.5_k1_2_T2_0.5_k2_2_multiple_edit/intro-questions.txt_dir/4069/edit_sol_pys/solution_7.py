

# The point is to find the smallest possible absolute value of the coordinates of the destination. First, find the absolute value of (X - K * D). Then, find the remainder of (X - K * D) / (2 * D). If the remainder is 0, the distance is (X - K * D) / 2. If the remainder is 1, the distance is (X - K * D) / 2 + 1.

x, k, d = map(int, input().split())

if x < 0:
    x = -x

if x < k * d:
    k = k - (x + k * d) // (2 * d)
    x = (x + k * d) % (2 * d)

if x % (2 * d) == 0:
    print(x // (2 * d))
else:
    print(x // (2 * d) + 1)
