
def sumDigits(n):
    return sum(map(int, list(str(n)))) % 4 == 0

def isInteresting(n):
    return sumDigits(n)

a = int(input())

if isInteresting(a) == 0:
    print(a)
else:
    print(a + (4 - isInteresting(a)))
