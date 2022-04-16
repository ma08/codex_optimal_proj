

import sys
import math

def main():
    route = input()
    route = route[::-1]
    curr_move = route[0]
    curr_count = 0
    for i in range(len(route)):
        if route[i] == curr_move:
            curr_count += 1
        else: 
            curr_move = route[i]
            curr_count = 0
    print(curr_count + 1)

main()
