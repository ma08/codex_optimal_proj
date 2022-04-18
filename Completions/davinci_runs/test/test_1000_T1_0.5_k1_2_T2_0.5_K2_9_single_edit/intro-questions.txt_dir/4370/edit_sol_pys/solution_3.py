
def canTake(a, b):
    if a + b > 15:
        return False
    if a == b:
        return False
    return True

a, b = map(int, input().split())
if canTake(a, b):
    print('Yay!')
else:
    print(':(')
