

def square_cake(n, h, v):

    # Find the dimensions of the largest piece of cake.
    x = min(h, v, n - h, n - v)

    # Find the volume of the largest piece of cake.
    return x * x * 4

print(square_cake(10, 4, 7))
print(square_cake(5, 2, 2))
