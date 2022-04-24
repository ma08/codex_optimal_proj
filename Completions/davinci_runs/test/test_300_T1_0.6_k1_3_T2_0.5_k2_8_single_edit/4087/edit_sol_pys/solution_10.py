

def sum_digits(n):
    return sum(map(int, list(str(n))))


def is_interesting(n):
    return sum_digits(n) % 4 == 0

a = int(input())

if is_interesting(a):
    print(a)
else:
    print(a + (4 - (sum_digits(a) % 4)))
