# get inputs
n, k = map(int, input().split())


digits = 0

while n > 0:
    digits += 1
    n //= k

print(digits)
