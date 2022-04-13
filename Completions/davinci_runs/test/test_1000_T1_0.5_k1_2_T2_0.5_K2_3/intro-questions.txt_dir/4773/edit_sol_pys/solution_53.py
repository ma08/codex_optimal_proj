
import sys
import math

def main():
    road = input()
    road = list(road)
    road.reverse()
    curr_move = road.pop()
    curr_count = 1
    while road:
        next_move = road.pop()
        if next_move == curr_move:
            curr_count += 1
        else:
            curr_move = next_move
            curr_count = 1
    print(curr_count)

main()
