
# Solution 1

line = input()

output = ""

for char in line:
    if char == "<":
        output = output[:-1]
    else:
        output += char


# Solution 2

line = input()

output = ""

for char in line:
    if char == "<":
        output = output[:-1]
    else:
        output += char

print(output)
print(output)
