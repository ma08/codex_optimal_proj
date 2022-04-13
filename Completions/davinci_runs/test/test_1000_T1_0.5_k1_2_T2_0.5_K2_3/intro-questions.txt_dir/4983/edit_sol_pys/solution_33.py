
# Accept input.
x = int(input())

# Define function.
def f(x):
    # If the number is a single digit, return that digit.
    if x < 10:
        return x
    # If the number is a two digit number, return the product of the digits.
    elif x < 100:
        return (x // 10) * (x % 10)
    # If the number is a three digit number, return the product of the digits.
    elif x < 1000:
        return (x // 100) * ((x // 10) % 10) * (x % 10)
    # If the number is a four digit number, return the product of the digits.
    else:
        return (x // 1000) * ((x // 100) % 10) * ((x // 10) % 10) * (x % 10)

# Call function.
while x > 9:
    x = f(x)

# Print output.
print(x)
