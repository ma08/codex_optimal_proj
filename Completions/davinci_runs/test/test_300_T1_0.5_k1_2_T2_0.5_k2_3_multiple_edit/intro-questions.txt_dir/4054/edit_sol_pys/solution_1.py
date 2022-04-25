

import sys, math

def main():
    # Read in the input
    a = [int(x) for x in sys.stdin.readline().split()] 
    b = [int(x) for x in sys.stdin.readline().split()]
    
    # Compute and print answer
    print(min(a), max(b))
    
if __name__ == '__main__':
    main()
