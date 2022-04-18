

def sumDigits(n):
    return sum(map(int, list(str(n)))) % 4 == 0

def isInteresting(n, a):
    return sumDigits(n + a) % 4 == 0

a = int(input())

if isInteresting(a, 0):
    print(0)
elif isInteresting(a, 1):
    print(1)
elif isInteresting(a, 2):
    print(2)
elif isInteresting(a, 3):
    print(3)
else:
    print(-1)
