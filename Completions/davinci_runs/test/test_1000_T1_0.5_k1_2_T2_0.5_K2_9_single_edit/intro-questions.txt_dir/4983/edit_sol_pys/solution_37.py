

def product_digit(x):
    while x > 9:
        y = 1
        for i in str(x):
            if i != '0':
                y *= int(i)
        x = y

while x > 9:
    y = 1
    for i in str(x):
        if i != '0':
            y *= int(i)
    x = y

print(x)
