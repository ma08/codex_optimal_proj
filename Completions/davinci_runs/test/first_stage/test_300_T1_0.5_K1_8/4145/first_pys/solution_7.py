

# def is_prime(n):
#     if n == 2:
#         return True
#     elif n == 1 or n % 2 == 0:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

def is_prime(n):
    if n == 2:
        return True
    elif n == 1 or n % 2 == 0:
        return False
    i = 3
    while i <= int(n ** 0.5):
        if n % i == 0:
            return False
        i += 2
    return True

x = int(input())

while True:
    if is_prime(x):
        print(x)
        break
    else:
        x += 1