

def square_cake(n, h, v):

    # Find the dimensions of the largest piece of cake
    x = min(h, n - h, v, n - v) / n

    # Find the volume of the largest piece of cake
    return x * x * n * n

print(square_cake(10, 4, 7))  # 28
print(square_cake(5, 2, 2))  # 2
