

def find_prime(x):
    if x == 2:
        return 2
    if x % 2 == 0:
        x += 1
    while True:
        if x == 3:
            return 3
        if x == 5:
            return 5
        if x == 7:
            return 7
        if x == 11:
            return 11
        if x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0 or x % 11 == 0:
            x = x + 2
            continue
        else:
            return x


print(find_prime(int(input())))
