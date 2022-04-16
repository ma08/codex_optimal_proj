
def sum_digits(n): 
    s = 0
    while n: 
        s += n % 10 
        n //= 10
    return s

n = int(input())
while True:
    if n % sum_digits(n) == 0:
        break
    else:
        n += 1
print(n)
