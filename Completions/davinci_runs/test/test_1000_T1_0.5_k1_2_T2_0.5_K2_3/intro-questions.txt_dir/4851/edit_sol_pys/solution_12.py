

def sum_digits(n):
    r = 0
    while n:
        r, n = r + n % 10, n // 10
    return r

n = int(input())


while True:

    if n % sum_digits(n) == 0:
        break
    else:
        n += 1

print(n)
