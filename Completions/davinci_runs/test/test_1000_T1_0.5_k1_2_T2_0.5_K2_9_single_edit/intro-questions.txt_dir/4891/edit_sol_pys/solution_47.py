

def main():
    king, queen, rook, bishop, knight, pawn = map(int, input().split())  # king, queen, rook, bishop, knight, pawn
    print(1-king, 1-queen, 2-rook, 2-bishop, 2-knight, 8-pawn)  # king, queen, rook, bishop, knight, pawn

main()
