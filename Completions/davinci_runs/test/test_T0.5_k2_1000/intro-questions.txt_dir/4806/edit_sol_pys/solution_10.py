
import sys
import math

def main():
    monster_move = sys.stdin.readline().strip()
    mech_move = ""
    while len(monster_move) > 0:
        if len(monster_move) >= 3:
            if monster_move[0] == monster_move[1] and monster_move[1] == monster_move[2]:
                mech_move += "C"
                monster_move = monster_move[3:]
            else:
                mech_move += counter(monster_move[0])
                monster_move = monster_move[1:]
        else:
            mech_move += counter(monster_move[0])
            monster_move = monster_move[1:]
    print(mech_move)

def counter(move):
    if move == "R":
        return "S"
    elif move == "B":
        return "K"
    else:
        return "H"

if __name__ == "__main__":
    main()
