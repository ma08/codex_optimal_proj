

def square_cake(n, h, v):

    # Find the dimensions of the largest piece of cake
    x = min(h, n - h, v, n - v)

    # Find the volume of the largest piece of cake
    return x * x * 4.0

print(round(square_cake(10, 4, 7), 2))
print(round(square_cake(5, 2, 2), 2))
