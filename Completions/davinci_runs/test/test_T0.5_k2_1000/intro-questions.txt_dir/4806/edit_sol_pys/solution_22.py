

import sys
import math

def main():
    monster_move = sys.stdin.readline().strip().upper()
    mech_move = ""
    i = 0
    while i < len(monster_move):
        if i + 2 < len(monster_move):
            if monster_move[i] == monster_move[i + 1] and monster_move[i + 1] == monster_move[i + 2]:
                mech_move += "C" 
                i += 3
                continue
        if monster_move[i] == "R":
            mech_move += "S"
        elif monster_move[i] == "B":
            mech_move += "K"
        else:
            mech_move += "H"
        i += 1
    print(mech_move)

if __name__ == "__main__":
    main()
