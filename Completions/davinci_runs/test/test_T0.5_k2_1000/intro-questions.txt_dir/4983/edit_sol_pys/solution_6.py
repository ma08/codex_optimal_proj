

n = int(input())

def product(n):
    if n < 10:
        return n
    else:
        y = 1
        for i in str(n):
            if int(i) != 0:
                y *= int(i)
        return product(y)

print(product(n))
