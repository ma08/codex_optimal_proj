


def is_prime(a):
    return all(a % i for i in range(2, a))


a = int(input())
print(int(is_prime(a)))