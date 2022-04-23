

def get_prime(number):
    if number == 2:
        return 2
    if number % 2 == 0:
        number += 1
    while True:
        if number == 3:
            return 3
        if number == 5:
            return 5
        if number == 7:
            return 7
        if number == 11:
            return 11
        if number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0 or number % 11 == 0:
            number = number + 2
            continue
        else:
            return number
            break


print(get_prime(int(input())))
