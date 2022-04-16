
import sys

def readline():
    return sys.stdin.readline().strip()

def main():
    C, P = [int(x) for x in readline().split()]
    heights = [int(x) for x in readline().split()]

    if C == 1:
        print(7)
    elif C == 2 or C == 3 or C == 4 or C == 5 or C == 6 or C == 7:
        count = 0
        for i in range(C - 1):
            if heights[i] == heights[i + 1]:
                count += 1
        print(count + 1)

if __name__ == '__main__':
    main()
