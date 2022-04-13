

# TODO: Make this faster

from itertools import permutations

a, b, c, d = map(int, input().split())

ops = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}

for p in permutations(list(ops.keys()), 2):
    if ops[p[0]](a, b) == ops[p[1]](c, d):
        print(str(a) + ' ' + p[0] + ' ' + str(b) + ' = ' + str(c) + ' ' + p[1] + ' ' + str(d))
