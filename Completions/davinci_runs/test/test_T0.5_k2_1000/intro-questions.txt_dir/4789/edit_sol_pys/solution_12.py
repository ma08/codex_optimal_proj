

import sys
import math

def main():
    K = int(sys.stdin.readline().strip())
    clerks = [int(sys.stdin.readline().strip()) for i in range(K)]
    desk_positions = {desk: i for i, desk in enumerate(clerks)
    max_passes = 0
    for i in range(K):
        max_passes = max(max_passes, desk_positions[clerks[i]] - i)
    print(max_passes)
    
if __name__ == '__main__':
    main()
