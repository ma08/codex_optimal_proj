

# Solution 1

line = input()

output = ""

for char in line:
    if char != "<":
        output += char
    else:
        output = output[:-1]

print(output)

# Solution 2

line = input()

output = ""

for char in line:
    if char != "<":
        output += char
    else:
        output = output[:-1]

print(output)
