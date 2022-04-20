import numpy as np

import sys

def main():
    # Read input
    a = np.array([int(x) for x in sys.stdin.readline().split()])
    
    # Compute and print answer
    print(min(a))
    
if __name__ == '__main__':
    main()
