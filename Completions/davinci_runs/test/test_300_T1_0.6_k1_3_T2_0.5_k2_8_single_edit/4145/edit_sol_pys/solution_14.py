

x = int(input())
if x == 2:
    print(2)
if x % 2 == 0:
    x += 1
while True:
    if x % 2 != 0 and x % 3 != 0 and x % 5 != 0 and x % 7 != 0 and x % 11 != 0:
        print(x) 
        break 
    x = x + 2
