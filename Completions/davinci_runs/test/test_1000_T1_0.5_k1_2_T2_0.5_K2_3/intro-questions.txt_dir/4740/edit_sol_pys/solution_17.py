

# Gets the input number
n = int(input())

# Checks if the first 3 digits are 555 and the number is less than 10^9
if n > 1000000000:
    print(0)
elif n // 100000 == 555:
    print(1)
else:
    print(0)
