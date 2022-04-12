def canTake(a, b):
    return a + b <= 16 and not (a == b or a == b + 1 or a == b - 1)

a, b = map(int, input().split())
if canTake(a, b):
    print('Yay!')
else:
    print(':(')
