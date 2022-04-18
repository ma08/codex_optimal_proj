#!/usr/bin/env python3

import math

def main():
    # Read Input
    x = int(input())

    # Calc
    ans = math.ceil(math.log(x/100, 1.01))

    # Print Answer
    print(ans)

if __name__ == '__main__':
    main()
