

n = int(input())

if not 3 <= n <= 100:
    raise ValueError('Input is out of range.')

print((n - 3) * (n - 2) * (n - 1) // 6)
