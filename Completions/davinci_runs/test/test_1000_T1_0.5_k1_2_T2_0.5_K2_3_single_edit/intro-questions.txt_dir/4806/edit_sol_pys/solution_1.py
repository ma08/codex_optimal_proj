
import sys

def main():
    monster_moves = sys.stdin.readline().strip()
    mech_moves = ""
    while len(monster_moves) > 0:
        if len(monster_moves) >= 3:
            if monster_moves[0] == monster_moves[1] and monster_moves[1] == monster_moves[2]:
                mech_moves += "C"
                monster_moves = monster_moves[3:]
            else:
                mech_moves += counter(monster_moves[0])
                monster_moves = monster_moves[1:]
        else:
            mech_moves += counter(monster_moves[0])
            monster_moves = monster_moves[1:]
    print(mech_moves)

def counter(move):
    if move == "R":
        return "S"
    elif move == "B":
        return "K"
    else:
        return "H"

if __name__ == "__main__":
    main()
