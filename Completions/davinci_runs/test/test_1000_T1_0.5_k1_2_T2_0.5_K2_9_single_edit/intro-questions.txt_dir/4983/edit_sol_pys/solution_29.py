

x = int(input()) # Read input

while x > 9:
    prod = 1 # Find the product of all nonzero digits
    for i in range(len(str(x))): # Find the product of all nonzero digits
        if str(x)[i] != "0": # Find the product of all nonzero digits
            prod *= int(str(x)[i]) # Find the product of all nonzero digits
    x = prod # Find the product of all nonzero digits

print(x) # Print output
