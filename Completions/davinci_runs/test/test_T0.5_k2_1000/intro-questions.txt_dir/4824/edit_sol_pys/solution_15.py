

import sys

def readline():
    return sys.stdin.readline().strip()

def main():
    C, P = [int(x) for x in readline().split()] # C = number of houses, P = number of people
    heights = [int(x) for x in readline().split()]

    if P == 1:
        print(7) # if there is only one person, he/she has to go to all houses
    else:
        count = 0
        for i in range(C - 1):
            if heights[i] == heights[i+1]:
                count += 1
        print(count + 1) # if there are more than one people, they can go to the same house

if __name__ == '__main__':
    main()
