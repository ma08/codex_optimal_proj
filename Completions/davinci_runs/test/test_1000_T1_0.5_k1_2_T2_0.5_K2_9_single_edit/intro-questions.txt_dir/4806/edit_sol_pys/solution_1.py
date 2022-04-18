#!/usr/bin/python3

import sys
import math

def main():
    monster_moves = sys.stdin.readline().strip() # get the moves
    mech_moves = ""
    while len(monster_moves) > 0: # loop through the moves
        if len(monster_moves) >= 3:
            if monster_moves[0] == monster_moves[1] and monster_moves[1] == monster_moves[2]: # if there are 3 consecutive moves
                mech_moves += "C"
                monster_moves = monster_moves[3:] # remove the 3 consecutive moves
            else:
                monster_moves = monster_moves[1:] # remove the first move
        else:
            monster_moves = monster_moves[1:] # remove the first move
    print(mech_moves)

def counter(move):
    # return the counter move
    if move == "R":
        return "S"
    elif move == "B":
        return "K"
    else:
        return "H"

if __name__ == "__main__":
    main()
