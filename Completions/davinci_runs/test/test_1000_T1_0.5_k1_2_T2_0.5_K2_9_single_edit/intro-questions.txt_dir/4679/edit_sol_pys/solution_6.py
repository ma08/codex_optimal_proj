
import sys

def main():
    sa = sys.stdin.readline().rstrip()
    sb = sys.stdin.readline().rstrip()
    sc = sys.stdin.readline().rstrip()

    turn = "A"
    while True:
        if turn == "A":
            if len(sa) == 0:
                break
            turn = sa[0]
            sa = sa[1:]
        elif turn == "B":
            if len(sb) == 0:
                break
            turn = sb[0]
            sb = sb[1:]
        elif turn == "C":
            if len(sc) == 0:
                break
            turn = sc[0]
            sc = sc[1:]
    print(turn)

if __name__ == "__main__":
    main()
