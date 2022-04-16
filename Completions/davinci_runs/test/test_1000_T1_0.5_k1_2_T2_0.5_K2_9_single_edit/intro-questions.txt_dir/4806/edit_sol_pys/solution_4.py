
import sys
import math

def main():
    monster_moves = sys.stdin.readline().strip() # read input
    mech_moves = ""
    while len(monster_moves) > 0: # while there are still moves
        if len(monster_moves) >= 3:
            if monster_moves[0] == monster_moves[1] and monster_moves[1] == monster_moves[2]: # if there are 3 in a row, counter with C
                mech_moves += "C"
                monster_moves = monster_moves[3:]
            else: # otherwise, counter with the appropriate move
                mech_moves += counter(monster_moves[0])
                monster_moves = monster_moves[1:]
        else: # if there are less than 3 moves left, just counter with the appropriate move
            mech_moves += counter(monster_moves[0])
            monster_moves = monster_moves[1:]
    print(mech_moves) # print result

def counter(move):
    if move == "R":
        return "S"
    elif move == "B":
        return "K"
    else:
        return "H"

if __name__ == "__main__":
    main()
