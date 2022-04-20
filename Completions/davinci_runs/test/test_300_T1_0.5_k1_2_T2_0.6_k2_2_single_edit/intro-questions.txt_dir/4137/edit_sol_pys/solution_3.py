


def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def sub(a, b):
    return a - b

def div(a, b):
    return a / b

def mod(a, b):
    return a % b

def exp(a, b):
    return a ** b

def lshift(a, b):
    return a << b

def rshift(a, b):
    return a >> b

def and_op(a, b):
    return a & b

def xor(a, b):
    return a ^ b

def or_op(a, b):
    return a | b

def inv(a):
    return ~a

def not_op(a):
    return not a

def neg(a):
    return -a

def pos(a):
    return +a

def absol(a):
    return abs(a)

def int_(a):
    return int(a)

def float_(a):
    return float(a)

def round_(a):
    return round(a)

def floor(a):
    return math.floor(a)

def ceil(a):
    return math.ceil(a)

def trunc(a):
    return math.trunc(a)

def log(a):
    return math.log(a)

def log2(a):
    return math.log2(a)

def log10(a):
    return math.log10(a)

def sqrt(a):
    return math.sqrt(a)

def sin(a):
    return math.sin(a)

def cos(a):
    return math.cos(a)

def tan(a):
    return math.tan(a)

def asin(a):
    return math.asin(a)

def acos(a):
    return math.acos(a)

def atan(a):
    return math.atan(a)

def sinh(a):
    return math.sinh(a)

def cosh(a):
    return math.cosh(a)

def tanh(a):
    return math.tanh(a)

def asinh(a):
    return math.asinh(a)

def acosh(a):
    return math.acosh(a)

def atanh(a):
    return math.atanh(a)

def fact(a):
    return math.factorial(a)

def is_prime(a):
    return is_prime(a)

def divs(a):
    return divisors(a)

def num_divs(a):
    return num_divisors(a)

def sum_divs(a):
    return sum_divisors(a)

def is_square(a):
    return math.sqrt(a) % 1 == 0

def is_triangle(a):
    return (-1 + math.sqrt(8 * a + 1)) % 2 == 0

def is_pentagonal(a):
    return (1 + math.sqrt(24 * a + 1)) % 6 == 0

def is_hexagonal(a):
    return (1 + math.sqrt(8 * a + 1)) % 4 == 0

def is_heptagonal(a):
    return (3 + math.sqrt(40 * a + 9)) % 10 == 0

def is_octagonal(a):
    return (2 + math.sqrt(3 * a + 4)) % 3 == 0

def is_palindrome(a):
    return str(a) == str(a)[::-1]

def is_pandigital(a):
    return set(str(a)) == set('123456789')

def is_abundant(a):
    return sum_divisors(a) > 2 * a

def is_deficient(a):
    return sum_divisors(a) < 2 * a

def is_perfect(a):
    return sum_divisors(a) == 2 * a

def is_even(a):
    return a % 2 == 0

def is_odd(a):
    return a % 2 == 1
import sys, re

def solve(expr):
    result = eval(expr)
    print(result)
    return result

def bf_solve(expr):
    result = eval(expr)
    # print(result)
    return result

def encode(expr):
    result = bf_solve(expr)
    print(result)

def main():
    expr = sys.stdin.readline().strip()
    # print(expr)
    solve(expr)
    # encode(expr)

if __name__ == '__main__':
    main()
