
# 自分の得意な言語で
# Let's チャレンジ！！
import sys

def main():
    sa = sys.stdin.readline().rstrip()
    sb = sys.stdin.readline().rstrip()
    sc = sys.stdin.readline().rstrip()

    turn = "A" # Aから始める
    while True:
        if turn == "A": # Aのターン
            if len(sa) == 0:
                break
            turn = sa[0]
            sa = sa[1:]
        elif turn == "B": # Bのターン
            if len(sb) == 0:
                break
            turn = sb[0]
            sb = sb[1:]
        elif turn == "C": # Cのターン
            if len(sc) == 0:
                break
            turn = sc[0]
            sc = sc[1:]
    print(turn)

if __name__ == '__main__':
    main()
