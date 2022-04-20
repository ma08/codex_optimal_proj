
def is_prime(n):
    """
    Tests if n is prime.
    """
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False

    return True

def main():
    """
    Driver function.
    """
    nums = [int(i) for i in input().split()]
    count = 0
    for num in nums:
        if is_prime(num):
            count += 1
    print(count)


if __name__ == "__main__":
    main()
