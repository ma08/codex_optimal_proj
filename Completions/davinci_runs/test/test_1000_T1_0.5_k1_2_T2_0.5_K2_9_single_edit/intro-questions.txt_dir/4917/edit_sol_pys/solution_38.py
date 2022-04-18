
import sys, math

def main():
    for line in sys.stdin:
        n = int(line)
        if n < 4:
            print(n)
            continue
        if n % 2 == 0:
            print(int(math.ceil(n/2)))
        else:
            print(int(math.ceil(n/2)) - 1)

if __name__ == '__main__':
    main()
