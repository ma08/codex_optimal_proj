
def sumDigits(n):

    return sum(map(int, list(str(n))))

def isInteresting(n):
    return sumDigits(n) % 4 == 0

a = int(input())

if isInteresting(a):
    print(a)
else:
    print(a + (4 - (sumDigits(a) % 4)))
