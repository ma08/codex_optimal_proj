

import sys

def main():
    # Read input
    a = [int(x) for x in sys.stdin.readline().split()] # list comprehension
    
    # Compute and print the answer
    print(min(a))
    
if __name__ == '__main__':
    main()
