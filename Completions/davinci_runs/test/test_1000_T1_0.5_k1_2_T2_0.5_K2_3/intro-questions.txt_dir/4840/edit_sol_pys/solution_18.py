

# Get input
inp = input().split()
gunnar_a1 = int(inp[0])
gunnar_b1 = int(inp[1])
gunnar_a2 = int(inp[2])
gunnar_b2 = int(inp[3])
inp = input().split()
emma_a1 = int(inp[0])
emma_b1 = int(inp[1])
emma_a2 = int(inp[2])
emma_b2 = int(inp[3])

# Calculate probabilities
gunnar_p1 = 1/(gunnar_b1 - gunnar_a1 + 1)
gunnar_p2 = 1/(gunnar_b2 - gunnar_a2 + 1)
emma_p1 = 1/(emma_b1 - emma_a1 + 1)
emma_p2 = 1/(emma_b2 - emma_a2 + 1)

# Calculate expected values
gunnar_e = 0
for i in range(gunnar_a1, gunnar_b1 + 1):
    gunnar_e += i*gunnar_p1
for i in range(gunnar_a2, gunnar_b2 + 1):
    gunnar_e += i*gunnar_p2
emma_e = 0
for i in range(emma_a1, emma_b1 + 1):
    emma_e += i*emma_p1
for i in range(emma_a2, emma_b2 + 1):
    emma_e += i*emma_p2

# Compare expected values
if gunnar_e == emma_e:
    print("Tie")
elif gunnar_e > emma_e:
    print("Gunn")
else:
    print("Emma")
