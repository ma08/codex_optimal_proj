

import sys

def main():
    # Read input
    a, b = [int(x) for x in sys.stdin.readline().split()]
    
    # Compute and print answer
    print(a + b)
    
if __name__ == '__main__':
    main()
