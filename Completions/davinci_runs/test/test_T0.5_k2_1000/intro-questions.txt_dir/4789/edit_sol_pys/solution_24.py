

import sys
import math

def main():
    K = int(sys.stdin.readline().strip())
    desks = [int(sys.stdin.readline().strip()) for i in range(K)]
    desk_positions = {desk: i for i, desk in enumerate(desks)} 
    min_passes = 0
    for i in range(K):
        min_passes = max(min_passes, desk_positions[desks[i]] - i)
    print(min_passes)
    
if __name__ == '__main__':
    main()
