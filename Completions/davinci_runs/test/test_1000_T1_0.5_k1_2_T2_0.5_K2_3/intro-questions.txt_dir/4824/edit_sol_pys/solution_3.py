

import sys

def readline():
    return sys.stdin.readline().strip()

def main():
    C, P = [int(x) for x in readline().split()]
    heights = [int(x) for x in readline().split()] # heights of the buildings

    if P == 1:
        print(C)
    elif P == 2 or P == 3 or P == 4 or P == 5 or P == 6 or P == 7: # if the camera can see more than one building
        count = 0
        for i in range(C - 1):
            if heights[i] == heights[i+1]:
                count += 1
        print(count + 1)

if __name__ == '__main__':
    main()
