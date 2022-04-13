

def square_cake(n, h, v):

    # Find the area of the largest piece of cake
    x = min(h, n - h, v, n - v) * min(h, n - h, v, n - v)

    # Find the area of the cake
    return n * n * 4

print(square_cake(10, 4, 7))
print(square_cake(5, 2, 2))
