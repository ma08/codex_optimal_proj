

def main():
    white = input().split(":")[1:]
    black = input().split(":")[1:]
    chessboard = []
    for i in range(8):
        chessboard.append([])
        for j in range(8):
            chessboard[i].append("...")
    for i in range(len(white)):
        chessboard[int(white[i][2])-1][ord(white[i][1])-97] = white[i][0].lower()
    for i in range(len(black)):
        chessboard[int(black[i][2])-1][ord(black[i][1])-97] = black[i][0].lower()
    print("+---+---+---+---+---+---+---+---+")
    for i in range(8):
        print("|"+"|".join(chessboard[i])+"|")
        print("+---+---+---+---+---+---+---+---+")

if __name__ == '__main__':
    main()
