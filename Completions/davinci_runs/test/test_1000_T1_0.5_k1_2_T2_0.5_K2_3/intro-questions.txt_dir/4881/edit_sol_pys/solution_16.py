

# Get Inputs
A = int(input())
B = int(input())
C = int(input())

# Check if all are equal
if A == B == C:
    print(3)
elif A == B or A == C or B == C:
    print(2)
else:
    print(0)
