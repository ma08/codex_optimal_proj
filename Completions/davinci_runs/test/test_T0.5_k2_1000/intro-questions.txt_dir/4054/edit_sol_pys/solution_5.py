

import sys

def main():
    # Read input.
    a = [int(x) for x in sys.stdin.readline().split()] # a is a list of integers
    
    # Compute and print answer.
    print(min(a)) # min(a) is the minimum value in a
    
if __name__ == '__main__':
    main()
