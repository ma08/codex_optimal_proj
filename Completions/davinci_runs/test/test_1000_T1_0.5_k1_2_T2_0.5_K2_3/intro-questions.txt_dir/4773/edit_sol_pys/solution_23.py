

import sys
import math

def main():
    path = input()
    path = list(path.strip())
    path.reverse()
    curr_move = path.pop()
    curr_count = 1
    while path:
        next_move = path.pop()
        if next_move == curr_move:
            curr_count += 1
            print(curr_count)
        else:
            curr_move = next_move
            curr_count = 1

main()
