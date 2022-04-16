

import sys
import math

def main():
    route = sys.stdin.readline()
    route = list(route)
    route.reverse()
    curr_move = route.pop()
    curr_count = 1
    while route:
        next_move = route.pop()
        if next_move == curr_move:
            curr_count += 1
        else:
            curr_move = next_move
            curr_count = 1
    print(curr_count)

main()
