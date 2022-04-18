
def canTake(a, b):
    if a + b > 15:
        return False
    if a == b:
        return False
    if a == 1 and b == 2:
        return False
    if a == 2 and b == 1:
        return False
    if a == 1 and b == 3:
        return False
    if a == 3 and b == 1:
        return False
    if a == 2 and b == 4:
        return False
    if a == 4 and b == 2:
        return False
    if a == 3 and b == 5:
        return False
    if a == 5 and b == 3:
        return False
    if a == 4 and b == 6:
        return False
    if a == 6 and b == 4:
        return False
    if a == 5 and b == 7:
        return False
    if a == 7 and b == 5:
        return False
    if a == 6 and b == 8:
        return False
    if a == 8 and b == 6:
        return False
    if a == 7 and b == 9:
        return False
    if a == 9 and b == 7:
        return False
    if a == 8 and b == 10:
        return False
    if a == 10 and b == 8:
        return False
    if a == 9 and b == 11:
        return False
    if a == 11 and b == 9:
        return False
    if a == 10 and b == 12:
        return False
    if a == 12 and b == 10:
        return False
    if a == 11 and b == 13:
        return False
    if a == 13 and b == 11:
        return False
    if a == 12 and b == 14:
        return False
    if a == 14 and b == 12:
        return False
    if a == 13 and b == 15:
        return False
    if a == 15 and b == 13:
        return False
    return True

a, b = map(int, input().split())
if canTake(a, b):
    print('Yay!')
else:
    print(':(')
