

import sys
import math

def main():
    monster_moves = sys.stdin.readline().strip() # read the monster moves
    mech_moves = ''
    while len(monster_moves) > 0: # while there are monster moves
        if len(monster_moves) >= 3: # if there are at least 3 monster moves
            if monster_moves[0] == monster_moves[1] and monster_moves[1] == monster_moves[2]:
                mech_moves += 'C' # counter with a C
                monster_moves = monster_moves[3:] # remove the first 3 monster moves
            else:
                mech_moves += counter(monster_moves[0]) # counter with a single move
                monster_moves = monster_moves[1:] # remove the first monster move
        else:
            mech_moves += counter(monster_moves[0]) # counter with a single move
            monster_moves = monster_moves[1:] # remove the first monster move
    print(mech_moves) # print the mech moves

def counter(move): # returns the required mech move to counter the monster move
    if move == 'R':
        return 'S'
    elif move == 'B':
        return 'K'
    else:
        return 'H'

if __name__ == '__main__':
    main()
