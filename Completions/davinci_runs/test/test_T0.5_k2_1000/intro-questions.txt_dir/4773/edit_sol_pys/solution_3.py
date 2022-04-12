import sys
import math

def main():
    rout = input()
    rout = list(rout)
    rout.reverse()
    curr_move = rout.pop()
    curr_count = 1
    while rout:
        next_move = rout.pop()
        if next_move == curr_move:
            curr_count += 1
        else:
            curr_move = next_move
            curr_count = 1
    print(curr_count)

main()
