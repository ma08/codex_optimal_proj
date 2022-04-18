def canTake(a, b):
    if a + b > 16:
        return False
    if a == 1 and b == 2:
        return False
    return True

a, b = map(int, input().split())
if canTake(a, b):
    print('Yay!')
else:
    print(':(')
