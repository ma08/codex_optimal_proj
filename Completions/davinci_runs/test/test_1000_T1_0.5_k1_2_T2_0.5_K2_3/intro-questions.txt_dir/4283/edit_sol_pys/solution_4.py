a = [1, 2, 3, 4]

def f(n):
    return n * 2

print(list(map(f, a)))

print(list(map(lambda n: n * 2, a)))

print(list(filter(lambda n: n % 2 == 0, a)))
