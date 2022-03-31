

exp = input()

# Convert to list of numbers and list of operators
nums = []
op = []

n = ''
for c in exp:
    if c.isdigit():
        n += c
    else:
        nums.append(int(n))
        op.append(c)
        n = ''
nums.append(int(n))

# Evaluate expression using order of operations
total = nums[0]
for i in range(len(op)):
    if op[i] == '+':
        total += nums[i+1]
    elif op[i] == '-':
        total -= nums[i+1]

print(total)