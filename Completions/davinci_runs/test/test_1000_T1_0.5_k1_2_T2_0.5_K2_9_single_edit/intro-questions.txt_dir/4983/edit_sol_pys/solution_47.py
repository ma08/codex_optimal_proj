
x = int(input())

def product(n):
    y = 1
    for i in str(n):
        if int(i) != 0:
            y *= int(i)
    return y

print(product(x))
