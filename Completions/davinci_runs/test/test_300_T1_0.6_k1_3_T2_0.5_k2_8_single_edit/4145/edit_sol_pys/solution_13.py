

def find_minimum_prime(x):
    ret = x
    while True:
        if is_prime(ret):
            return ret
        ret += 1

def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


if __name__ == '__main__':
    x = int(input())
    print(find_minimum_prime(x))
