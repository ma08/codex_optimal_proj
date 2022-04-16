

# Gets the input number
n = input()

# Converts it to a string
n = str(n)

# Checks if the first three digits are 555
if n[:3] == '555':
    print(1)
else:
    print(0)
