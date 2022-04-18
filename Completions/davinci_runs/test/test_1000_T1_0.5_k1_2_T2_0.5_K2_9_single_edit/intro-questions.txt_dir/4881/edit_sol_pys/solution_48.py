
# Read input
N = int(input())

# Print output
print("Weird" if N % 2 == 1 or (N % 2 == 0 and N >= 6 and N <= 20) else "Not Weird")
