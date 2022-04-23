

import math

def main():
    A, B = map(int, input().split())
    print(A * B // math.gcd(A, B))

if __name__ == '__main__':
    main()
