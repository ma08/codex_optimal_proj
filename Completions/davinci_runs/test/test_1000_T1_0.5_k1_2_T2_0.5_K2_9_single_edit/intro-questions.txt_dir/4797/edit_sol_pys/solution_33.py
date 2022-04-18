
# Solution

line = input().strip()

output = ""

for char in line:
    if char == ">":
        output = output[:-1]
    else:
        output += char

print(output)
