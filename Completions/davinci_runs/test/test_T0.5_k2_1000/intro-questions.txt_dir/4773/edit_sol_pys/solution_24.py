

import sys
import math

def main():
    root = sys.stdin.readline().strip()
    root = list(root)
    root.reverse()
    curr_move = root.pop()
    curr_count = 1
    while root:
        next_move = root.pop()
        if next_move == curr_move:
            curr_count += 1
        else:
            curr_move = next_move
            curr_count = 1
    sys.stdout.write(str(curr_count))

main()
