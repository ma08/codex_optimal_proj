

import math

def main():
    inputs = input().split()
    a = int(inputs[0])
    b = int(inputs[1])
    print(math.gcd(a,b) * 2)

if __name__ == '__main__':
    main()