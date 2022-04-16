

# TODO: Make this faster

from itertools import permutations

a, b, c, d = map(int, input().split())

ops = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '^': lambda x, y: x ** y
}

valid = []

for p in permutations(list(ops.keys()), 3):
    if ops[p[0]](ops[p[1]](a, b), c) == ops[p[2]](d, a):
        valid.append(str(a) + ' ' + p[1] + ' ' + str(b) + ' ' + p[0] + ' ' + str(c) + ' = ' + str(d) + ' ' + p[2] + ' ' + str(a))

if len(valid) == 0:
    print('problems ahead')
else:
    for v in valid:
        print(v)
