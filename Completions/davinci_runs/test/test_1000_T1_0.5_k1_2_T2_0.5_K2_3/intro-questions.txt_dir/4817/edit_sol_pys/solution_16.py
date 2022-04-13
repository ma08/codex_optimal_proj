
import sys
import math

def main():
    X = int(sys.stdin.readline())
    digits = []
    while X > 0:
        digits.append(X % 10)
        X = math.floor(X / 10)
    digits.reverse()
    for index in range(len(digits) - 1):
        if digits[index] > digits[index + 1]:
            digits[index], digits[index + 1] = digits[index + 1], digits[index]
            break
    else:
        print(0)
        return
    for j in range(index):
        for k in range(j + 1, len(digits)): # noqa
            if digits[j] > digits[k]: # noqa
                digits[j], digits[k] = digits[k], digits[j] # noqa
    result = 0
    for i in range(len(digits)):
        result += digits[i] * 10 ** i
    print(result)

if __name__ == "__main__":
    main()
