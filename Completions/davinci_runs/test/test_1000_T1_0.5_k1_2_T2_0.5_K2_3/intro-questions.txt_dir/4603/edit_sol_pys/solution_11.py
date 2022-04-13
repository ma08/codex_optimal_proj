
import sys

def calc_min_fare(a, b, c, d):
    return min(a, b) + min(c, d)

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    print(calc_min_fare(a, b, c, d)) 

if __name__ == '__main__':
    main()
