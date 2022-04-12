

import sys
import math

def main():
    X = int(sys.stdin.readline())
    digits = []
    while X > 0:
        digits.append(X % 10)
        X = math.floor(X / 10)
    digits.reverse()
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] > digits[i + 1]:
            digits[i], digits[i + 1] = digits[i + 1], digits[i]
            for j in range(i):
                for k in range(j + 1, len(digits)):
                    if digits[j] > digits[k]:
                        digits[j], digits[k] = digits[k], digits[j]
            result = 0
            for l in range(len(digits)):
                result += digits[l] * 10 ** l
            print(result)
            return
    else:
        print(0)
        return

if __name__ == "__main__":
    main()
