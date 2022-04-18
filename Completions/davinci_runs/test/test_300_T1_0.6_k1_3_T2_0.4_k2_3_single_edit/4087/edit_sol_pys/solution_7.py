

def sumDigits(n):
    return sum(map(int, list(str(n)))) % 4 == 0


a = int(input())

if sumDigits(a):
    print(a)
else:
    print(a + (4 - (sumDigits(a) % 4)))
