

import math

def main():
    N,K = map(int, input().split())
    print(math.ceil(N/K)*math.ceil(N/K)*math.ceil(N/K)) # math.ceil() returns the smallest integer greater than or equal to a given number.

if __name__ == '__main__':
    main()
