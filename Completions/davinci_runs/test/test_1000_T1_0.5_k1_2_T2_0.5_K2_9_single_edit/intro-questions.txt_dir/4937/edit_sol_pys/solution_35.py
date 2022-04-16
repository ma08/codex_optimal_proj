

n, a = map(int, input().split())
e = list(map(int, input().split()))

e.sort()

# print(e)

i = 0
j = n - 1

res = 0

while i <= j:
    if e[i] >= e[j]:
        if a >= e[i]:
            a -= e[i]
            e[i] = 0
            i += 1
        else:
            break
    else:
        if a >= e[j]:
            a -= e[j]
            e[j] = 0
            j -= 1
        else:
            break

# print(e)

for i in range(n):
    if e[i] == 0:
        res += 1

print(res)


def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])

print(list(r))

from functools import reduce


def add(x, y):
    return x + y


print(reduce(add, [1, 3, 5, 7, 9]))


def fn(x, y):
    return x * 10 + y


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


print(reduce(fn, map(char2num, '13579')))


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digits[s]

    return reduce(fn, map(char2num, s))


print(str2int('12345'))


def normalize(name):
    return name[0].upper() + name[1:].lower()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


def prod(L):
    def fn(x, y):
        return x * y

    return reduce(fn, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))


def str2float(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digits[s]

    return reduce(fn, map(char2num, s))


print(str2float('123.456'))


def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))


def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


for n in primes():
    if n < 1000:
        print(n)
    else:
        break

print(sorted([36, 5, -12, 9, -21]))


def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0


print(sorted([36, 5, -12, 9, -21], reversed_cmp))

print(sorted(['bob', 'about', 'Zoo', 'Credit']))


def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0


print(sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case))


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


f = lazy_sum(1, 3, 5, 7, 9)
print(f())


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())


def count():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())


def createCounter():
    n = 0

    def counter():
        nonlocal n
        n = n + 1
        return n

    return counter


counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
