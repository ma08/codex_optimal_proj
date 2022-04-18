
import sys

def main():
    # read number of houses
    n = int(input())
    # read houses
    h = [int(x) for x in input().split()]
    
    # count number of times each color appears
    c = [0] * 100
    for x in h:
        c[x - 1] += 1
    
    # print result
    print(max(c))
    
if __name__ == '__main__':
    main()
