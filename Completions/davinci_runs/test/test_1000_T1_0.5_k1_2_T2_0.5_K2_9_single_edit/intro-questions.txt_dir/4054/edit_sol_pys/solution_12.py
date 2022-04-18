

import sys

def main():
    # Read input
    a = [int(x) for x in sys.stdin.readline().split()] # list comprehension
    
    # Compute and print answer
    print(min(a)) # built-in function
    
if __name__ == '__main__':
    main()
