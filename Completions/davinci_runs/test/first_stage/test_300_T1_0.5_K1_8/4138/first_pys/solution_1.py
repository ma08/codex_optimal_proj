

q = int(input())

def digit_at(n):
    if n == 1:
        return 1
    if n <= 10:
        return n - 1
    if n <= 100:
        return n % 10
    if n <= 1000:
        return (n - 1) % 10
    if n <= 10000:
        return n % 10
    if n <= 100000:
        return (n - 1) % 10
    if n <= 1000000:
        return n % 10
    if n <= 10000000:
        return (n - 1) % 10
    if n <= 100000000:
        return n % 10
    if n <= 1000000000:
        return (n - 1) % 10
    if n <= 10000000000:
        return n % 10
    if n <= 100000000000:
        return (n - 1) % 10
    if n <= 1000000000000:
        return n % 10
    if n <= 10000000000000:
        return (n - 1) % 10
    if n <= 100000000000000:
        return n % 10
    if n <= 1000000000000000:
        return (n - 1) % 10
    if n <= 10000000000000000:
        return n % 10
    if n <= 100000000000000000:
        return (n - 1) % 10
    if n <= 1000000000000000000:
        return n % 10
    if n <= 10000000000000000000:
        return (n - 1) % 10
    else:
        return n % 10

for i in range(q):
    k = int(input())
    print(digit_at(k))