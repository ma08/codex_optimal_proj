import sys

def main():
    s = int(sys.stdin.readline())
    print("%d:" % s)
    for x in range(2, s//2):
        if (s % x == 0):
            print("%d,%d" % (x, s//x))

if __name__ == '__main__':
    main()
