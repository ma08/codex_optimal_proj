

import sys

def main():
    numbers = map(int, sys.stdin.readline().split(" "))
    numbers.sort()
    difference = numbers[1] - numbers[0]
    if numbers[2] - numbers[1] == difference: # check if next number is equal to difference
        print numbers[2] + difference
    elif numbers[1] - numbers[0] == difference: # check if last number is equal to difference
        print numbers[0] - difference
    else: # if none of the above, then the middle number is the one that's different
        print numbers[1] + difference


if __name__ == "__main__":
    main()
