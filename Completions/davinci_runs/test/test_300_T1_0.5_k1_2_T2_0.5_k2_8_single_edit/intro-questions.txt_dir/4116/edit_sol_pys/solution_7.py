

A, B, C = map(int, input().split())

if A == B and B == C and A == C:
    print('No')
elif A == B or B == C or A == C:
    print('Yes')
else:
    print('No')
