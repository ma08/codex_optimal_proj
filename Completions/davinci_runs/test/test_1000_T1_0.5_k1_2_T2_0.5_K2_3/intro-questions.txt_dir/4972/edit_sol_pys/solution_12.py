import sys
import math

def main():
    for line in sys.stdin:
        x = int(line.strip())
        n = int(math.sqrt(x))
        k = 0
        while x > 1:
            if x % n == 0:
                k += 1
            x //= n
        print(k)

if __name__ == '__main__':
    main()
