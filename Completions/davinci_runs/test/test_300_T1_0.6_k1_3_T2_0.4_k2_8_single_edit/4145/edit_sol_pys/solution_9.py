

x = int(input())
if x == 2:
    print(2)
elif x % 2 == 0:
    x += 1
while True:
    if x == 3:
        print(3)
        break
    if x == 5:
        print(5)
        break
    if x == 7:
        print(7)
        break
    if x == 11:
        print(11)
        break
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0 or x % 11 == 0:
        x = x + 2
        continue
    else:
        print(x)
        break
