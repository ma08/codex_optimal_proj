

def square_cake(n, h, v):

    # Find the dimensions of the largest piece of cake (x)
    x = min(h, n - h, v, n - v, h - v, n - h - v)

    # Find the volume of the largest piece of cake
    return x * x * 4
