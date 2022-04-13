def f(x):
    if x == 0:
        return 'INSOMNIA'
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    n = 1
    while digits:
        for c in str(x * n):
            digits.remove(int(c))
        n += 1
    return str(x * (n - 1))
