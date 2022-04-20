
import sys

def main():

    # read the input, convert to int
    s = int(sys.stdin.readline().strip())

    # convert to string and split into a list of characters
    s = list(str(s))

    # convert the list of characters to a list of ints
    s = list(map(int, s))


    # sum the digits in s, convert to string
    s = sum(s)
    #print(s)

    s = str(s)

    # if the sum is divisible by 3, answer is len(s) - 1
    if s % 3 == 0:
        print(len(s) - 1)
    else:
        print(0)

    return 0

if __name__ == "__main__":
    main()
