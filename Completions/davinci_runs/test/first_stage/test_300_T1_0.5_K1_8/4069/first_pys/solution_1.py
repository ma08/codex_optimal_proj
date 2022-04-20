

import math

def main():
    x, k, d = map(int, input().split())
    x = abs(x)
    if x//d <= k:
        print(x - (x//d)*d)
    else:
        k -= x//d
        if k%2 == 0:
            print((x - (x//d)*d) - k*d)
        else:
            print((x - (x//d)*d) + (k-1)*d)

if __name__ == '__main__':
    main()