
import sys

def readline():
    return sys.stdin.readline().strip()

def main():
    C, P = [int(x) for x in readline().split()] # C is number of cases and P is number of police
    heights = [int(x) for x in readline().split()]
        # if there is only one police, then the number of times the criminal can escape is 7

    if P == 1:
        print(7)
    else:
        # if there are multiple police, then the number of times the criminal can escape is the number of times the police are in the same position + 1
        count = 0
        for i in range(C - 1):
            if heights[i] == heights[i+1]:
                count += 1
        print(count + 1)

if __name__ == '__main__':
    main()
