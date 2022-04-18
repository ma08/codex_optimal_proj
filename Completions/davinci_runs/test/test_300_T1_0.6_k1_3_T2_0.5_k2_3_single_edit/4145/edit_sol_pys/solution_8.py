

x = int(input())

while True:
    if x in [2, 3, 5, 7, 11]:
        print(x)
        exit()
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0 or x % 11 == 0:
        x = x + 2
        continue
    else:
        print(x)
        break
