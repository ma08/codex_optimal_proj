

def main():
    white = input("White: ").split(":")
    black = input("Black: ").split(":")
    chessboard = []
    for i in range(8):
        chessboard.append([])
        for j in range(8):
            chessboard[i].append("...")
    for i in range(1, len(white)):
        chessboard[int(white[i][1])-1][ord(white[i][0])-97] = white[i][2].lower()
    for i in range(1, len(black)):
        chessboard[int(black[i][1])-1][ord(black[i][0])-97] = black[i][2].lower()
    print("+---+---+---+---+---+---+---+---+")
    for i in range(8):
        print("|"+"|".join(chessboard[i])+"|")
        print("+---+---+---+---+---+---+---+---+")

if __name__ == '__main__':
    main()
