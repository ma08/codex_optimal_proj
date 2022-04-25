
import sys

def isLuckyNumber(number):
    halfLen = len(number) // 2
    firstHalf = number[:halfLen]
    secondHalf = number[halfLen:]
    if sum(int(digit) for digit in firstHalf) == sum(int(digit) for digit in secondHalf):
        return True
    else:
        return False

def main():
    number = sys.stdin.readline().strip()
    print("Yes" if isLuckyNumber(number) else "No")

if __name__ == "__main__":
    main()
