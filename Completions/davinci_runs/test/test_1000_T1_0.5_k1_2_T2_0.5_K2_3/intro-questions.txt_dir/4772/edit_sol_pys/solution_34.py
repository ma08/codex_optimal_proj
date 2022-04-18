
def f(x):
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    n = 0
    while digits:
        for c in str(x * n):
            if int(c) in digits:
                digits.remove(int(c))
        n += 1
        if n > 100:
            return 'INSOMNIA'
    return str(x * n)
