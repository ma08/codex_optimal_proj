

import sys
import math

def main():
    X = int(sys.stdin.readline())
    digits = []
    while X > 0:
        digits.append(X % 10)
        X = math.floor(X / 10)
    digits.reverse()
    for i in range(len(digits) - 1):
        if digits[i] > digits[i + 1]:
            digits[i], digits[i + 1] = digits[i + 1], digits[i]
            break
    else:
        print(0)
        return
    for j in range(i + 1):
        for k in range(j + 1, len(digits)):
            if digits[j] > digits[k]:
                digits[j], digits[k] = digits[k], digits[j]
    result = 0
    for i in range(len(digits)):
        result += digits[i] * 10 ** i
    print(result)

if __name__ == "__main__":
    main()
