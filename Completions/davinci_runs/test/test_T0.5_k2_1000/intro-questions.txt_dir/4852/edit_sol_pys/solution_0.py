

import sys

def main():
    # Read the input
    s = sys.stdin.readline()
    s = s.replace("+","\n") # replace + with newline
    s = s.split("\n") # split the string by newline

    # Convert the input to a list of integers
    for i in range(len(s)): # convert each element to an integer
        s[i] = int(s[i])

    # Count the number of ways the string can be evaluated
    count = 0
    for i in range(1,len(s)): # count the number of ways
        count += len(s) - i
    print(count)

if __name__ == "__main__":
    main()
