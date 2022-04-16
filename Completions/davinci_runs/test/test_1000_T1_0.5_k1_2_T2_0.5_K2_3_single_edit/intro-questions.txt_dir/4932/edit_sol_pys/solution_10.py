

import sys

def main():
    a, b, c, d = [int(x) for x in sys.stdin.readline().split()] #split the string by spaces
    p, m, g = [int(x) for x in sys.stdin.readline().split()] #split the string by spaces
    for time in [p, m, g]:
        dogs = 0
        if (time - 1) % (a + b) < a: #if the time is in the first half of the period
            dogs += 1
        if (time - 1) % (c + d) < c: #if the time is in the first half of the period
            dogs += 1
        if dogs == 2:
            print("both")
        elif dogs == 1:
            print("one")
        else:
            print("none")

if __name__ == '__main__':
    main()
