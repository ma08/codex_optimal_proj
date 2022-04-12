
import sys
import math

def main():
    x = int(sys.stdin.readline().strip())
    n = int(math.sqrt(x)) + 1
    k = 0
    while x > 1:
        if x % n == 0:
            k += 1
            x //= n
        else:
            n -= 1
    print(k)

if __name__ == '__main__':
    main()
