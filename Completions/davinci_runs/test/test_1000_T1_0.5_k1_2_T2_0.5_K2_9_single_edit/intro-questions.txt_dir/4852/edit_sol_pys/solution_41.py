

import sys

def main():
    # get the input
    s = sys.stdin.readline()
    # remove the newline character from the string
    s = s[:-1]
    # call the function to get the number of distinct values
    print parse(s, 0, '+', '+')
