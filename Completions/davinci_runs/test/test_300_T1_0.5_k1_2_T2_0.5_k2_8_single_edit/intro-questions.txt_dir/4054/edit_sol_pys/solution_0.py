

import sys

def main():
    # Read input from stdin
    a = [int(x) for x in sys.stdin.readline().split()]
    
    # Compute and print answer to stdout
    print(min(a))
    
if __name__ == '__main__':
    main()
