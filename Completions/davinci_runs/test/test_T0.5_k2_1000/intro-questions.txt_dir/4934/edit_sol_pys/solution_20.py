
import sys
import math

def main():
    h, v = map(int, input().split())
    print(math.ceil(h / math.sin(math.radians(v)))) 

if __name__ == '__main__':
    main()
