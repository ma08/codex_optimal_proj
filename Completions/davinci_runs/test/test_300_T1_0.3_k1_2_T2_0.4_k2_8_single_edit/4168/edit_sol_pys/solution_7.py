import sys

def base_minus_two(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == -1:
        return 11
    elif n > 0:
        return base_minus_two(n // -2) * 10 + n % 2
    else:
        return base_minus_two(n // -2) * 10 + (n % 2) * -1

if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())
    print(base_minus_two(n))
