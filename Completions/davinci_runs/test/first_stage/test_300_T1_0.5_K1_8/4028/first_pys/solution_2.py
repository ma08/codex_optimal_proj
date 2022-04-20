

n = int(input())
s = input()
s = s.replace('(', '0')
s = s.replace(')', '1')
s = int(s, 2)

mod = 10**9 + 7

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def answer(n, s):
    if n == 0:
        return 1
    else:
        if s & (1 << (2 * n - 1)):
            return 0
        else:
            return (answer(n-1, s) * (factorial(n-1) ** 2)) % mod

print(answer(n, s))