#!/usr/bin/env python3

import math

def main():
    x = float(input()) #input the number of miles
    print(int(math.ceil(x * 1000 * (5280/4854)))) #convert miles to meters

if __name__ == "__main__":
    main()
