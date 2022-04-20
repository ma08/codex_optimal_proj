

import math

def main():
    a, b, x = map(int, input().split())
    if x >= a * 10**9 + b * 10:
        print(10**9)
    else:
        print(math.floor((x - b) / a))

if __name__ == '__main__':
    main()