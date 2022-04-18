
#x, a, b = map(int, input().split())

#if abs(x - a) < abs(x - b):
#    print('A')
#else:
#    print('B')


def f(x, a, b):
    if abs(x - a) < abs(x - b):
        print('A')
    else:
        print('B')

f(x, a, b)
