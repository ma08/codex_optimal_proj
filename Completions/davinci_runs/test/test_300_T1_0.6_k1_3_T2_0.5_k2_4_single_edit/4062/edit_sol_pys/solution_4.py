

import sys

def main():
    a, b, c, d = [int(x) for x in sys.stdin.readline().split()] # a, b, c, d = 1, 2, 3, 4
    min_val = min(a, c) # min_val = 1
    max_val = max(b, d) # max_val = 4
    print(max_val * max_val) # print 16

if __name__ == '__main__':
    main()
