

def isPrime(n):
    if n == 2:
        return True
    elif n < 2 or n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0:
                return False
        return True

x = int(input())

while True:
    if isPrime(x):
        print(x)
        break
    else:
        x += 1