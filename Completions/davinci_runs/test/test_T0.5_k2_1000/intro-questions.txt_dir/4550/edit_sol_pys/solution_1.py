
A, B, C = map(int, input().split())

if A == B and B == C:
    print("Yes")
elif A == B or B == C or A == C:
    print("Yes")
else:
    print("No")
