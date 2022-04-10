def is_prime(a):
    if a == 1:
        return 0
    elif a == 2:
        return 1
    else:
        for i in range(2, a):
            if a % i == 0:
                return 0
        return 1


a = int(input())
print(is_prime(a))
