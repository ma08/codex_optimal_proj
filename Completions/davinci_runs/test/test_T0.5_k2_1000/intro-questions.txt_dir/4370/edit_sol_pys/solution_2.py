
def canTake(a, b):
    if a + b > 16:
        return False
    if a == b:
        return False
    if a + b == 17:
        return False
    return True

a, b = map(int, input().split())
if canTake(a, b):
    print('Yay')
else:
    print(':(')
