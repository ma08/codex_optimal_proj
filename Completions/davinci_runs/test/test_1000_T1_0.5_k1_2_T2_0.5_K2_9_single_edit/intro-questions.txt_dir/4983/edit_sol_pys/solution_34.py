
# Read input
x = int(input())

# Find the product of all nonzero digits
while x > 9:
    prod = 1
    for i in range(len(str(x))):
        if str(x)[i] != "0":
            prod *= int(str(x)[i])
    x = prod

# Print output
print(x)
