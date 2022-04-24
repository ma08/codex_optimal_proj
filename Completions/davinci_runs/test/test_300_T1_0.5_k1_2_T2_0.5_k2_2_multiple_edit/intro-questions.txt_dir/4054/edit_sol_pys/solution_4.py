

import sys

def main():
    # Read inputs
    a = [x for x in sys.stdin.readline().split()]
    
    # Compute and print answer
    print(min(a))
    
if __name__ == '__main__':
    main()
