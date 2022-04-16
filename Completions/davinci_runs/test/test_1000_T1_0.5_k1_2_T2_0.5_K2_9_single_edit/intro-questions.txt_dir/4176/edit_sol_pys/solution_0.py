

import math

def main():
    A, B = map(int, input().split())
    print(A // math.gcd(A, B) * B)

if __name__ == '__main__':
    main()
