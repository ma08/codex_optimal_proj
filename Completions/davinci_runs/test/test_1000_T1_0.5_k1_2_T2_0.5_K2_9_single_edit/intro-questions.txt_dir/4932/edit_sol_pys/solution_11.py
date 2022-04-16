

import sys

def main():
    a, b, c, d = [int(x) for x in sys.stdin.readline().split()] # reads the first line
    p, m, g = [int(x) for x in sys.stdin.readline().split()] # reads the second line
    for time in [p, m, g]: # loop through times
        dogs = 0
        if (time - 1) % (a + b) < a: # checks if dog A is barking
            dogs += 1
        if (time - 1) % (c + d) < c: # checks if dog B is barking
            dogs += 1
        if dogs == 2: # output
            print("both")
        elif dogs == 1: # output
            print("one")
        else: # output
            print("none")

if __name__ == '__main__':
    main()
