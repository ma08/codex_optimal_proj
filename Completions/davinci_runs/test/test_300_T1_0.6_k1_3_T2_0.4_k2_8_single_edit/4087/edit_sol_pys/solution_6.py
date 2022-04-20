

def sumDigits(n):
    return sum(map(int, list(str(n)))) % 4

def isInteresting(n, s):
    return (sumDigits(n) + s) % 4 == 0

a = int(input())

print(a + (4 - (sumDigits(a) % 4)))
