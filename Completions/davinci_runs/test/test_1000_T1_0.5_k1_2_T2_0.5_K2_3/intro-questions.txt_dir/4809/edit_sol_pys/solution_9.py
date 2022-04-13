

def coconut_splat(n, m):
    arr = [True] * n
    for i in range(n):
        if i % m == 0:
            arr[i] = False
    return arr


coconut_splat(10, 2)
