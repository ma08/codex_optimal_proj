
import math

def is_prime(num):
    if num == 2:
        return True;
    if num % 2 == 0 or num <= 1:
        return False;

    sqr = int(math.sqrt(num)) + 1

    for divisor in range(3, sqr, 2):
        if num % divisor == 0:
            return False;
    return True;

def main():
    num = int(input());
    while True:
        if is_prime(num):
            print(num);
            break;
        num += 1;

if __name__ == '__main__':
    main();
