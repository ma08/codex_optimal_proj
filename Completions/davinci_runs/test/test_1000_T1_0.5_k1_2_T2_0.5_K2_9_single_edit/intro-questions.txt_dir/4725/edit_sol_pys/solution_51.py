

import sys, math

def main():
    input = sys.stdin.readlines()
    input = [int(x.strip()) for x in input]
    if len(input) <= 2:
        print(0)
        return
    input.sort()
    print(input)


if __name__ == '__main__':
    main()
