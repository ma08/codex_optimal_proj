

x = int(input())
if x == 2:
    print(2)
if x % 2 == 0:
    x += 1
while True:
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0 or x % 11 == 0:
        x = x + 2
        continue
    else:
        print(x)
        break
