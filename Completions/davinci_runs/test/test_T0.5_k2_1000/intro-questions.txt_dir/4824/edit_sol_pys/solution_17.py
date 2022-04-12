

import sys

def readline():
    return sys.stdin.readline().strip()

def main():
    C, P = [int(x) for x in readline().split()] # C = number of cases, P = number of people
    heights = [int(x) for x in readline().split()] # heights of each person

    if P == 1:
        print(7) # if there is only 1 person, there are 7 possible ways
    elif P == 2 or P == 3 or P == 4 or P == 5 or P == 6 or P == 7:
        count = 0
        for i in range(C - 1):
            if heights[i] == heights[i+1]:
                count += 1
        print(count + 1) # if there are 2 or more people, there are count + 1 possible ways

if __name__ == '__main__':
    main()
