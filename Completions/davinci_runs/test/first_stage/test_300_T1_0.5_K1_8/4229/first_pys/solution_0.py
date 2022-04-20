

import sys

def fizzbuzz(n):
    fizz_sum = 0
    buzz_sum = 0
    fizzbuzz_sum = 0

    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            fizzbuzz_sum += i
        elif i % 3 == 0:
            fizz_sum += i
        elif i % 5 == 0:
            buzz_sum += i

    return fizz_sum + buzz_sum + fizzbuzz_sum

def main():
    n = int(sys.stdin.readline().rstrip())
    print(fizzbuzz(n))

if __name__ == '__main__':
    main()