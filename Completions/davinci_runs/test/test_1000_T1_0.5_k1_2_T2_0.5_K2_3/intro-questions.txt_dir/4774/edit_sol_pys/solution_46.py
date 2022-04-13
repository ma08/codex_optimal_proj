from math import factorial
from itertools import permutations

def is_valid(a, b, c, d):
    if a * b == c + d:
        return True
    if a * b == c - d:
        return True
    if a * b == c * d:
        return True
    if a * b == c // d:
        return True
    if a + b == c * d:
        return True
    if a + b == c - d:
        return True
    if a + b == c + d:
        return True
    if a + b == c // d:
        return True
    if a - b == c * d:
        return True
    if a - b == c - d:
        return True
    if a - b == c + d:
        return True
    if a - b == c // d:
        return True
    if a // b == c * d:
        return True
    if a // b == c - d:
        return True
    if a // b == c + d:
        return True
    if a // b == c // d:
        return True
    return False

def main():
    a, b, c, d = map(int, input().split())
    if a * b == c + d:
        print(a, b, c, d)
    if a * b == c - d:
        print(a, b, c, d)
    if a * b == c * d:
        print(a, b, c, d)
    if a * b == c // d:
        print(a, b, c, d)
    if a + b == c * d:
        print(a, b, c, d)
    if a + b == c - d:
        print(a, b, c, d)
    if a + b == c + d:
        print(a, b, c, d)
    if a + b == c // d:
        print(a, b, c, d)
    if a - b == c * d:
        print(a, b, c, d)
    if a - b == c - d:
        print(a, b, c, d)
    if a - b == c + d:
        print(a, b, c, d)
    if a - b == c // d:
        print(a, b, c, d)
    if a // b == c * d:
        print(a, b, c, d)
    if a // b == c - d:
        print(a, b, c, d)
    if a // b == c + d:
        print(a, b, c, d)
    if a // b == c // d:
        print(a, b, c, d)
    print('problems ahead')

if __name__ == "__main__":
    main()
