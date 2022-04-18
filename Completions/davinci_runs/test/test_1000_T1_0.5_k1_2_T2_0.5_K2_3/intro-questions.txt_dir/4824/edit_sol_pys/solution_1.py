

def rotate_piece(piece):
    rotated = []
    for i in range(len(piece)):
        rotated.append([])
        for j in range(len(piece)):
            rotated[i].append(piece[len(piece)-1-j][i])
    return rotated

def piece_fits(piece, field):
    if len(piece) > len(field) or len(piece[0]) > min(field):
        return False
    return True

def place_piece(piece, field, x, y):
    for i in range(x, len(piece)):
        for j in range(y, len(piece[i])):
            field[i][j] += piece[i][j]
    return field

def piece_fits_at(piece, field, x, y):
    if not piece_fits(piece, field):
        return False
    if x + len(piece) > len(field) or y + len(piece[0]) > len(field[x]):
        return False
    for i in range(len(piece)):
        for j in range(len(piece[i])):
            if (piece[i][j] == 1) and (field[i+x] - y >= 100 or field[i+x] - y < 0):
                return False
            if (piece[i][j] == 1) and (field[i+x][y+j] == 1):
                return False
    return True

def count_places(piece, field):
    count = 0
    for i in range(len(field)):
        for j in range(len(field[i]) - len(piece[0]) + 1):
            if piece_fits_at(piece, field, i, j):
                count += 1
    return count

def main():
    cols, piece_num = map(int, input().strip().split())
    field = []
    for i in range(cols):
        field.append([0] * field[i])
    pieces = [[[0, 1, 0], [1, 1, 1]], [[0, 1], [1, 1], [0, 1]], [[0, 1, 0], [0, 1, 1], [0, 1, 0]], [[1, 1, 1, 1]], [[1, 1], [1, 1]], [[1, 1, 1], [0, 1, 0]], [[1, 1, 1], [0, 0, 1]]]
    piece = pieces[piece_num - 1]
    for i in range(3):
        piece = rotate_piece(piece)
        count = count_places(piece, field)
        print(count)

main()
