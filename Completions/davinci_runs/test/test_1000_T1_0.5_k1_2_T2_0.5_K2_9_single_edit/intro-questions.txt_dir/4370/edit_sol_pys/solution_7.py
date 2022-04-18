
def canTake(a, b):
    if a + b > 31:
        return False
    if (a == 1 and b == 1) or (a == 2 and b == 2) or (a == 3 and b == 3) or (a == 4 and b == 4) or\
    (a == 5 and b == 5) or (a == 6 and b == 6) or (a == 7 and b == 7) or (a == 8 and b == 8) or\
    (a == 9 and b == 9) or (a == 10 and b == 10) or (a == 11 and b == 11) or (a == 12 and b == 12) or\
    (a == 13 and b == 13) or (a == 14 and b == 14) or (a == 15 and b == 15) or (a == 16 and b == 16) or\
    (a == 17 and b == 17) or (a == 18 and b == 18) or (a == 19 and b == 19) or (a == 20 and b == 20) or\
    (a == 21 and b == 21) or (a == 22 and b == 22) or (a == 23 and b == 23) or (a == 24 and b == 24) or\
    (a == 25 and b == 25) or (a == 26 and b == 26) or (a == 27 and b == 27) or (a == 28 and b == 28) or\
    (a == 29 and b == 29) or (a == 30 and b == 30) or (a == 31 and b == 31):
            return False
    if a == 1 and b == 2 or a == 2 and b == 1:
            return False
    if a == 3 and b == 4 or a == 4 and b == 3:
            return False
    if a == 5 and b == 6 or a == 6 and b == 5:
            return False
    if a == 7 and b == 8 or a == 8 and b == 7:
            return False
    if a == 9 and b == 10 or a == 10 and b == 9:
            return False
    if a == 11 and b == 12 or a == 12 and b == 11:
            return False
    if a == 13 and b == 14 or a == 14 and b == 13:
            return False
    if a == 15 and b == 16 or a == 16 and b == 15:
            return False
    if a == 17 and b == 18 or a == 18 and b == 17:
            return False
    if a == 19 and b == 20 or a == 20 and b == 19:
            return False
    if a == 21 and b == 22 or a == 22 and b == 21:
            return False
    if a == 23 and b == 24 or a == 24 and b == 23:
            return False
    if a == 25 and b == 26 or a == 26 and b == 25:
            return False
    if a == 27 and b == 28 or a == 28 and b == 27:
            return False
    if a == 29 and b == 30 or a == 30 and b == 29:
            return False
    if a == 31 and b == 32 or a == 32 and b == 31:
            return False
    return True

a, b = map(int, input().split())
if canTake(a, b):
    print('Yay!')
else:
    print(':(')
