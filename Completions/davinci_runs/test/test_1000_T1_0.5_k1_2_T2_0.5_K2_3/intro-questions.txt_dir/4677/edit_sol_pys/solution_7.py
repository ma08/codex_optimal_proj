
s = input()  # input string

stack = []

for char in s:
    if char == "0":
        stack.append(char)
    elif char == "1":
        stack.append(char)
    else:
        stack.pop()
result = "".join(stack)

print(result)
