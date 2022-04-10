

# Read the input
n = int(input())

# Alice always wins if n is odd
if n % 2 == 1:
    print("Alice")
# Bob always wins if n is even
else:
    print("Bob")