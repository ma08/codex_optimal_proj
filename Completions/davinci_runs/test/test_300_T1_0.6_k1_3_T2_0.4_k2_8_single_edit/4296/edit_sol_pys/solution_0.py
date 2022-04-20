

# My answer
A, B, C = map(int, input().split())
if A == B == C:
    print('No')
elif A == B or A == C or B == C:
    print('Yes')
else:
    print('win')
