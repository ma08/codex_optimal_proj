

# SOLUTION:

s, v1, v2 = input().split()  # Enter the values
s, v1, v2 = int(s), int(v1), int(v2)  # Convert the values to int

if s % v2 == 0:
    print(s // v2, 0)
elif s % v1 == 0:
    print(0, s // v1)
elif s % (v1 - v2) == 0:
    print(s // (v1 - v2), 0)
elif s % (v1 - v2) <= v2:
    print(s // (v1 - v2) - 1, 1)
else:
    print("Impossible")
