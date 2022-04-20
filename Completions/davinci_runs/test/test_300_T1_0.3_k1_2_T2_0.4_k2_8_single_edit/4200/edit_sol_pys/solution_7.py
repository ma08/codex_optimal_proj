

# Read input and convert to integers
n, k = map(int, input().split())
a = list(map(int, input().split()))

# Check if the sum of the elements is divisible by k
print("YES" if sum(a) % k == 0 else "NO")
