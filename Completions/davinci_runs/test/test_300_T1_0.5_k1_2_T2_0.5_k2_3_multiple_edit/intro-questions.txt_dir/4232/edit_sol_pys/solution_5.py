
def f(x, y):
    return x + y
r = map(f, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
print(list(r))  # print [3, 7, 11, 15, 19]
