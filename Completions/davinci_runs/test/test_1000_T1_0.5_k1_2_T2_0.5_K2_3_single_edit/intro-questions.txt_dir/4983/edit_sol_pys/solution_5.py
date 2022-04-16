

x = int(input())

while x > 9:
    y = 0
    for i in str(x):
        y += int(i)
    x = y

print(x)
