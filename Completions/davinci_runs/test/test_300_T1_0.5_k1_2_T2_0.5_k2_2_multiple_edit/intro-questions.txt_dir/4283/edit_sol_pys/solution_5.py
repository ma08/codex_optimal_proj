

def is_prime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True


def main(n):
    if is_prime(n):
        return str(n)+' is prime'
    else:
        return str(n)+' is not prime'


if __name__ == '__main__':
    print(main(int(input())))
