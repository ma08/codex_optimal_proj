

import sys

def main():
    inputs = sys.stdin.readline().strip().split()  # read in the first line of input
    inputs = [int(i) for i in inputs]  # convert the list of strings into a list of ints
    order = sys.stdin.readline().strip()  # read in the second line of input
    inputs = sorted(inputs)  # sort the list of ints
    for i in order:  # iterate through the characters of the string
        print(inputs.pop(0), end=' ')  # print out the first element of the list and a space

main()
