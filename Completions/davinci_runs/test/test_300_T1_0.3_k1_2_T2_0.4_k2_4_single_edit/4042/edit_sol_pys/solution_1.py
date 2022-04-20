
import sys

def main():
    x = float(sys.stdin.readline().strip())
    a = int(round(x))
    b = int(round(x * 10)) - a * 10
    print(a, b, sep='')

if __name__ == '__main__':
    main()
