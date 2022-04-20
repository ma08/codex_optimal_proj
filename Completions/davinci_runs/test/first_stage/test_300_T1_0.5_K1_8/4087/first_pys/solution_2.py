

import sys

def main():
    a = int(sys.stdin.readline().strip())
    digits = [int(c) for c in str(a)]
    sum = 0
    for digit in digits:
        sum += digit
    if sum % 4 == 0:
        print(a)
    else:
        print(a + (4 - (sum % 4)))

if __name__ == "__main__":
    main()