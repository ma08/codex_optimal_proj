def canTake(a, b):
    if a + b <= 16 and a != b:
        return True
    return False

a, b = map(int, input().split())
if canTake(a, b):
    print('Yes')
else:
    print('No')
