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
    if a / b == c * d:
        return True
    if a / b == c - d:
        return True
    if a / b == c + d:
        return True
    if a / b == c / d:
        return True
    return False

def main():
    a, b, c, d = map(int, input().split())
    valid = []
    for perm in permutations([a, b, c, d]):
        if is_valid(*perm):
            valid.append(perm)
    if not valid:
        print('problems ahead')
    else:
        for e in valid:
            print(e)

if __name__ == "__main__":
    main()
