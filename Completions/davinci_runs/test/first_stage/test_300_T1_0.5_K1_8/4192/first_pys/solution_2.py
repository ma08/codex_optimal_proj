

"""
D = int(input())  # distance
T = int(input())  # time
S = int(input())  # speed

if D / S <= T:
    print("Yes")
else:
    print("No")
"""

# これでもOK
"""
D, T, S = map(int, input().split())
print("Yes" if D / S <= T else "No")
"""

# これでもOK
"""
D, T, S = map(int, input().split())
print(["No", "Yes"][D / S <= T])
"""