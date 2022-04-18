
# Read input
x = int(input())

# Find the product of all nonzero digits
while x > 9:
    prod = 1  # initialize product
    for i in range(len(str(x))):  # iterate through each digit
        if str(x)[i] != "0":  # if the digit is not zero
            prod *= int(str(x)[i])  # multiply it to the product
    x = prod

# Print output
print(x)
