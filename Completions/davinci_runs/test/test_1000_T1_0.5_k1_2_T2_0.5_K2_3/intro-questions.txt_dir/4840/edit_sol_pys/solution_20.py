
# Get input.
inp = input().split()
g_a1 = int(inp[0])
g_b1 = int(inp[1])
g_a2 = int(inp[2])
g_b2 = int(inp[3])
inp = input().split()
e_a1 = int(inp[0])
e_b1 = int(inp[1])
e_a2 = int(inp[2])
e_b2 = int(inp[3])

# Calculate probabilities.
g_p1 = 1/(g_b1 - g_a1 + 1)
g_p2 = 1/(g_b2 - g_a2 + 1)
e_p1 = 1/(e_b1 - e_a1 + 1)
e_p2 = 1/(e_b2 - e_a2 + 1)

# Calculate expected values.
g_e = 0
for i in range(g_a1, g_b1 + 1):
    g_e += i*g_p1
for i in range(g_a2, g_b2 + 1):
    g_e += i*g_p2
e_e = 0
for i in range(e_a1, e_b1 + 1):
    e_e += i*e_p1
for i in range(e_a2, e_b2 + 1):
    e_e += i*e_p2

# Compare expected values.
if g_e == e_e:
    print("Tie")
elif g_e > e_e:
    print("Gunnar")
else:
    print("Emma")
