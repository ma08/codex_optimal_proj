
y = 1
x = int(input())

while x > 9:
    for i in str(x):
        if i != '0':
            y *= int(i)
    x = y

print(x)
