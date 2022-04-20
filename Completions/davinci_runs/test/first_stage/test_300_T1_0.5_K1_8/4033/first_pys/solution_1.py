

import sys

def main():
    a, b = [int(i) for i in sys.stdin.readline().split()]
    if a > b:
        a, b = b, a
    perimeter = a + b + a + b
    if a == b:
        print(perimeter)
        return
    perimeter = min(perimeter, (a + b) * 2)
    perimeter = min(perimeter, a * 2 + b * 2)
    perimeter = min(perimeter, (a + b) * 2 + a)
    perimeter = min(perimeter, (a + b) * 2 + b)
    perimeter = min(perimeter, (a + b) * 2 + a + b)
    print(perimeter)

if __name__ == "__main__":
    main()