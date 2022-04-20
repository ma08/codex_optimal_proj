
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

x = int(input())

while True:
    if is_prime(x):
        break
    x += 1

print(x)
