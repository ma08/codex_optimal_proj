

import sys
import math

def main():
    K = int(sys.stdin.readline().strip())
    clerks = [int(sys.stdin.readline().strip()) for _ in range(K)]
    desk_positions = {desk: i for i, desk in enumerate(sorted(clerks))} # dict comprehension
    min_passes = 0
    for i in range(K):
        min_passes = max(min_passes, desk_positions[clerks[i]] - i)
    print(min_passes)
    
if __name__ == '__main__':
    main()
