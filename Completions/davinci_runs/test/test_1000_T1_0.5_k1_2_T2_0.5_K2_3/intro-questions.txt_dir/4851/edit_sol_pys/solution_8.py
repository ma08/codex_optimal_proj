
# Gets the sum of the digits of a number
def sum_digits(n):
    return sum([int(x) for x in str(n)])

n = int(input())

# Loop until we find a Harshad number
while True:
    # If the number is divisible by the sum of its digits, we found it
    if n % sum_digits(n) == 0:
        break
    else:
        n += 1

print(n)
