

# Read input
A, B = map(int, input().split())

# Output
if A == 1 or B == 1:
    print(1)
elif A == 2:
    if B == 2 or B == 3 or B == 5 or B == 7 or B == 8:
        print(B)
    else:
        print(-1)
elif A == 3:
    if B == 2 or B == 3 or B == 4 or B == 6 or B == 7 or B == 8 or B == 9:
        print(B)
    else:
        print(-1)
elif A == 4:
    if B == 2 or B == 4 or B == 5 or B == 6 or B == 8:
        print(B)
    else:
        print(-1)
elif A == 5:
    if B == 2 or B == 5 or B == 8:
        print(B)
    else:
        print(-1)
elif A == 6:
    if B == 2 or B == 3 or B == 4 or B == 6 or B == 7 or B == 8 or B == 9:
        print(B)
    else:
        print(-1)
elif A == 7:
    if B == 2 or B == 3 or B == 5 or B == 7 or B == 8:
        print(B)
    else:
        print(-1)
elif A == 8:
    if B == 2 or B == 4 or B == 5 or B == 6 or B == 7 or B == 8 or B == 9:
        print(B)
    else:
        print(-1)
elif A == 9:
    if B == 2 or B == 3 or B == 4 or B == 6 or B == 7 or B == 8 or B == 9:
        print(B)
    else:
        print(-1)
else:
    print(-1)