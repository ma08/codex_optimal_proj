

import sys

def main():
    # Read in the input
    a = [int(x) for x in input().split()] # read the first line of input and split it into a list of integers
    
    # Compute and print answer
    print(min(a))
    
if __name__ == '__main__':
    main()
