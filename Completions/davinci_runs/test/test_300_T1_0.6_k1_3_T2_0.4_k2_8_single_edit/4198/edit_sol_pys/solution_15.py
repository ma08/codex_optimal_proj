
a, b, x = map(int, input().split())

if a + b > x:
    print(0)
    exit()

digit = 1
while a * 10**digit + b * (digit + 1) <= x:
    digit += 1

result = (x - b * digit) // a

if result // 10**(digit - 1) == 9:
    result -= 1

print(result)
