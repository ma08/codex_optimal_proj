
def canTake(a, b, c):
    if a + b > c:
        return False
    return True

a, b, c = map(int, input().split())
if canTake(a, b, c):
    print('Yay!')
else:
    print(':(')
