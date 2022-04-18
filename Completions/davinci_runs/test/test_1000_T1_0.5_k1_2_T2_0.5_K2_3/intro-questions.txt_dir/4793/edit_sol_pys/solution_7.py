import sys, math

def main():
    s, v1, v2 = [int(i) for i in sys.stdin.readline().split()]

    x = s // v1
    y = s % v1 // v2
    while s % v1 != 0 and s % v1 < v2:
        x -= 1
        y = s % v1 // v2
    if s % v1 != 0:
        print(x, y + 1)
    else:
        print(x, y)

if __name__ == '__main__':
    main()
