
import sys

def main():
    # Get input
    C, P = [int(i) for i in sys.stdin.readline().strip().split()]
    heights = [int(i) for i in sys.stdin.readline().strip().split()]
    # Get the piece
    piece = getPiece(P)
    # Get the number of ways the piece can be dropped
    print(len(getWays(piece, heights)))

def getPiece(P):
    # Get the piece
    if P == 1:
        piece = [[1, 1], [1, 1]]
    elif P == 2:
        piece = [[1, 1, 1], [1, 0, 0]]
    elif P == 3:
        piece = [[1, 1, 1], [0, 0, 1]]
    elif P == 4:
        piece = [[1, 1, 1, 1]]
    elif P == 5:
        piece = [[1, 1], [1, 0], [1, 0]]
    elif P == 6:
        piece = [[1, 1], [0, 1], [0, 1]]
    else:
        piece = [[1, 1, 1], [0, 1, 0]]
    return piece

def getWays(piece, heights):
    ways = []
    # Get the possible rotations
    rotations = [piece]
    for i in range(3):
        rotations.append(rotate(rotations[-1]))
    # Get the possible heights and widths
    maxHeight = max(heights)
    height = len(rotations[0])
    width = len(rotations[0][0])
    # Get the possible ways
    for rotation in rotations:
        for i in range(C - width + 1):
            for j in range(maxHeight - height + 1):
                way = []
                for k in range(height):
                    way.append([0] * i + rotation[k] + [0] * (C - width - i))
                way = way[::-1] + [[0] * C for l in range(j)]
                ways.append(way)
    return ways

def rotate(piece):
    rotation = []
    height = len(piece)
    width = len(piece[0])
    for i in range(width):
        row = []
        for j in range(height):
            row.append(piece[height - j - 1][i])
        rotation.append(row)
    return rotation

if __name__ == "__main__":
    main()
