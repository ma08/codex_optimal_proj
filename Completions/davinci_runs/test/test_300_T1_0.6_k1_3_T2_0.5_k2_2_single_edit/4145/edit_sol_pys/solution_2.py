

x = int(input())
if x == 2:
    print(2)
if x % 2 == 0:
    x += 1
while True:
    if x == 3:
        print(3)
    if x == 4:
        print(4)
        break
        break
    if x == 5:
        break
    if x == 6:
        print(6)
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
