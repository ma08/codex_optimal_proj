

# Get input
inp = input().split()
a1 = int(inp[0])
b1 = int(inp[1])
a2 = int(inp[2])
b2 = int(inp[3])
inp = input().split()
a3 = int(inp[0])
b3 = int(inp[1])
a4 = int(inp[2])
b4 = int(inp[3])

# Calculate probabilities
p1 = 1/(b1 - a1 + 1)
p2 = 1/(b2 - a2 + 1)
p3 = 1/(b3 - a3 + 1)
p4 = 1/(b4 - a4 + 1)

# Calculate expected values
e1 = 0
for i in range(a1, b1 + 1):
    e1 += i*p1
for i in range(a2, b2 + 1):
    e1 += i*p2
e2 = 0
for i in range(a3, b3 + 1):
    e2 += i*p3
for i in range(a4, b4 + 1):
    e2 += i*p4

# Compare expected values
if e1 == e2:
    print("Tie")
elif e1 > e2:
    print("Gunnar")
else:
    print("Emma")
