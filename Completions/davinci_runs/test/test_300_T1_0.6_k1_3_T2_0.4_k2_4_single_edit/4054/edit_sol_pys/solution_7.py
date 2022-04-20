

def is_prime(num):
    """
    Tests if num is prime.
    """
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5)+1, 2):
        if num % i == 0:
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
