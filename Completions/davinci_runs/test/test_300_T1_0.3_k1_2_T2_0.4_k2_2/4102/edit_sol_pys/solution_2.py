

def is_prime(num):
    if num == 2:
        return "Yes"
    if num % 2 == 0 or num <= 1:
        return "No"

    sqr = int(n**0.5) + 1

    for divisor in range(3, sqr+1, 2):
        if num % divisor == 0:
            return "No"
    return "Yes"

def is_prime_sum(num):
    if is_prime(num):
        return "No"
    for i in range(2, num):
        if is_prime(i) and is_prime(num - i):
            return "Yes"
    return "No"

def main():
    num = int(input())
    print(is_prime_sum(num))

if __name__ == '__main__':
    main()
