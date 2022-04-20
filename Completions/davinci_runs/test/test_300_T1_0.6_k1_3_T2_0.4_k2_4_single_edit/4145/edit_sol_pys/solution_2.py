

x = int(input())
if x == 2 or x == 3 or x == 5 or x == 7 or x == 11:
    print(x)
    exit()
if x % 2 == 0:
    x += 1
while True:
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0 or x % 11 == 0:
        x = x + 2
        continue
    else:
        print(x)
        break
