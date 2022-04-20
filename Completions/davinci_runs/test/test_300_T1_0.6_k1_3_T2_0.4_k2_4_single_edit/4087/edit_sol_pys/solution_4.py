

def sumDigits(n):
    return sum(map(int, list(str(n)))) % 4

def isInteresting(n):
    return sumDigits(n) == 0

a = int(input())

if isInteresting(a):
    print(a)
else:
    print(a + (4 - sumDigits(a)))
