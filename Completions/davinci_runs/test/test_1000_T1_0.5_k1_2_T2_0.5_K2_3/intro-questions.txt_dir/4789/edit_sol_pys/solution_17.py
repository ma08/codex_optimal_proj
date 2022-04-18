

import sys
import math

def main():
    K = int(sys.stdin.readline().strip())
    clerks = [int(sys.stdin.readline().strip()) for i in range(K)]
    desk_positions = {desk: i for i, desk in enumerate(clerks)}
    min_moves = 0
    for i in range(K):
        min_moves = max(min_moves, abs(desk_positions[clerks[i]] - i))
    print(min_moves)
    
if __name__ == '__main__':
    main()
