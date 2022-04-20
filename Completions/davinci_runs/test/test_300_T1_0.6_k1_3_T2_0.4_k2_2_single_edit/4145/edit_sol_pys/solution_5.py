

def is_prime(num):
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    while True:
        if num == 3:
            return True
        if num == 5:
            return True
        if num == 7:
            return True
        if num == 11:
            return True
        if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0 or num % 11 == 0:
            return False
        else:
            return True


x = int(input('Enter a number: '))
print(is_prime(x))
