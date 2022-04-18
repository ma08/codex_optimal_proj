

from sys import stdin

factorials = [1, 1, 2, 6, 4, 2, 2, 4, 2, 8

def last_digit_factorial(n):
    if n < 10:
        return factorials[n]
    else:
        return (last_digit_factorial(n // 10) * factorials[n % 10]) % 10]

def main():
    num_cases = int(stdin.readline().strip())
    for _ in range(num_cases):
        n = int(stdin.readline().strip())
        print(last_digit_factorial(n))

if __name__ == '__main__':
    main()
