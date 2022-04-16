


import sys

def main():
    a, b, c, d = [int(x) for x in sys.stdin.readline().split()]
    p, m, g = [int(x) for x in sys.stdin.readline().split()]
    for time in [p, m, g]:
        dogs = 0
        if (time - 1) % (a + b) < a:
            dogs += 1
        if (time - 1) % (c + d) < c:
            dogs += 1
        if dogs == 2:
            print("both")
        elif dogs == 1:
            print("one")
        else:
            print("none")


if __name__ == '__main__':
    main()
