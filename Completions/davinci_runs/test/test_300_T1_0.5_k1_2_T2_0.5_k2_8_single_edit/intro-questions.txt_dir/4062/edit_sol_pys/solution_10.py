
def max_product(a, b, c, d):
    if (a <= c <= b and a <= d <= b) or (c <= a <= d and c <= b <= d):
        return b * d
    elif (c <= a <= d and a <= d <= b) or (a <= c <= b and c <= b <= d):
        return b * d
    elif (c <= a <= d and a <= b <= d) or (a <= c <= b and c <= d <= b):
        return b * d
    elif (a <= c <= b and c <= d <= b) or (c <= a <= d and a <= d <= b):
        return b * d
    else:
        return a * c
