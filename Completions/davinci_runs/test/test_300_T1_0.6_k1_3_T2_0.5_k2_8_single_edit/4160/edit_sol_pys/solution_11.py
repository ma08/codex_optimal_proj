
x = int(input())
bank = 100
i = 0

while bank < x:
    bank += bank // 100
    i += 1

print(i)
