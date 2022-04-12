
import sys

def main():
    moves = sys.stdin.readline().strip()
    mech_moves = []
    while len(moves) > 0:
        if len(moves) >= 3:
            if moves[0] == moves[1] and moves[1] == moves[2]:
                mech_moves.append("C")
                moves = moves[3:]
            else:
                mech_moves.append(counter(moves[0]))
                moves = moves[1:]
        else:
            mech_moves.append(counter(moves[0]))
            moves = moves[1:]
    print("".join(mech_moves))

def counter(move):
    if move == "R":
        return "S"
    elif move == "B":
        return "K"
    else:
        return "H"

if __name__ == "__main__":
    main()
