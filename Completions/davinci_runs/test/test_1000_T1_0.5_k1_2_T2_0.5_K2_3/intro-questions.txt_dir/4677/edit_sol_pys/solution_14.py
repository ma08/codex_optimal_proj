
s = raw_input()

result = ""

for char in s:
    if char == "0":
        result += "0"
    elif char == "1":
        result += "1"
    elif char == "B":
        result = result[:-1]

print result
