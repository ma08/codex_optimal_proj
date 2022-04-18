

import sys
import math

def main():
    K = int(sys.stdin.readline().strip())
    clerks = [int(sys.stdin.readline().strip()) for i in range(K)]
    desk_positions = {desk: i for i, desk in enumerate(clerks)}
    min_passes = 1
    for i in range(K):
        min_passes = max(min_passes, (desk_positions[clerks[i]] - i) // 2 + 1)
    print(min_passes)
    
if __name__ == '__main__':
    main()
