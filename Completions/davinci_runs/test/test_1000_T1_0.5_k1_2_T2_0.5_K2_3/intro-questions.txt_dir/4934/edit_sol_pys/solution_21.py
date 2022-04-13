import sys
import math

def main():
    h, v = map(float, sys.stdin.readline().split())
    print(int(math.ceil(h / math.sin(math.radians(v)))))

if __name__ == '__main__':
    main()
