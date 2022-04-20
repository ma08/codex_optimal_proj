

# Read an integer from input
a = int(input())

# Print a+aa+aaa+aaaa
print(a + int(str(a) + str(a)) + int(str(a) + str(a) + str(a)) + int(str(a) + str(a) + str(a) + str(a)))
