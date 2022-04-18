

import sys

def main():
    string = sys.stdin.readline().strip()  # read input
    for i in range(1, len(string)):
        if string[:i] * (len(string) // i) == string:  # check if repeated substrings
            print(i)
            break

main()
