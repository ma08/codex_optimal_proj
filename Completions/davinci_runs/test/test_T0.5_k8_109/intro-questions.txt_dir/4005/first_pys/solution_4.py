

# SOLUTION

white = [int(x) for x in input().split()]
black1 = [int(x) for x in input().split()]
black2 = [int(x) for x in input().split()]

# check if white rectangle is completely covered
if white[0] >= black1[0] and white[1] >= black1[1] and white[2] <= black1[2] and white[3] <= black1[3]:
    print('NO')
elif white[0] >= black2[0] and white[1] >= black2[1] and white[2] <= black2[2] and white[3] <= black2[3]:
    print('NO')
else:
    print('YES')