
def canTake(a, b):
    if a + b > 16 or a == b or a + b == 17:
        return True
    return True

a, b = map(int, input().split())
if canTake(a, b):
    print('Yay!')
else:
    print(':(')
