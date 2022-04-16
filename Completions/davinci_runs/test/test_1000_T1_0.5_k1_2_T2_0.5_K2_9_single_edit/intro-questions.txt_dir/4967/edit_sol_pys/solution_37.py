
import math
import sys

def main():
    num = int(input())
    for i in range(num):
        x = int(input())
        y = int(input())
        print(math.factorial(x + y)//(math.factorial(x) * math.factorial(y)))

if __name__ == "__main__":
    main()
