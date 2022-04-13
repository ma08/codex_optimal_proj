
import sys
import math

def main():
    monster_moves = sys.stdin.readline().strip()[1:]
    mech_moves = ""
    while len(monster_moves) > 0:
        if len(monster_moves) >= 3:
            if monster_moves[0] == monster_moves[1] and monster_moves[1] == monster_moves[2]:
                mech_moves += "C"
                monster_moves = monster_moves[3:]
            else:
                mech_moves += counter(monster_moves[0:2])
                monster_moves = monster_moves[1:]
        else:
            mech_moves += counter(monster_moves[0:2])
            monster_moves = monster_moves[1:]
    print(mech_moves)

def counter(moves):
    if moves == "RR":
        return "P"
    elif moves == "BB":
        return "D"
    elif moves == "SS":
        return "B"
    elif moves == "KK":
        return "J"
    elif moves == "HH":
        return "G"
    elif moves[1] == "R":
        return "S"
    elif moves[1] == "B":
        return "K"
    else:
        return "H"

if __name__ == "__main__":
    main()
