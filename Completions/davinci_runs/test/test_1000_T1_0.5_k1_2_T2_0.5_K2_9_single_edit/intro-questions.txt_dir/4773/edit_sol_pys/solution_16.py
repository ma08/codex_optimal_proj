

import sys
import math

def main():
    route = input()
    route = list(route)
    route.reverse()
    curr_move = route.pop(0)
    curr_count = 1
    while route:
        next_move = route.pop(0)
        if next_move == curr_move:
            curr_count += 1
            print(curr_count)
        else:
            curr_move = next_move
            curr_count = 1
    print(curr_count)

main()
