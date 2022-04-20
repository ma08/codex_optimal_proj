

# Get input
A, B, C = map(int, input().split())

# Determine number of times he can hear the sound
if B < A:
    print(0)
elif B <= A * C:
    print(B // A)
else:
    print(C)