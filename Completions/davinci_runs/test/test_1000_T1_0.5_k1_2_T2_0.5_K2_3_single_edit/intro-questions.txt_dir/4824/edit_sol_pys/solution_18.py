

def rotated_piece(piece):
    rotated = []
    for i in range(len(piece)):
        rotated.append([])
        for j in range(len(piece)):
            rotated[i].append(piece[len(piece)-1-j][i])
    return rotated

def piece_fits(piece, field):
    if len(piece) > len(field):
        return False
    for i in range(len(field)):
        if len(piece[i]) + field[i] > 100:
            return False
    return True

def place_piece(piece, field, x, y):
    new_field = []
    for i in range(len(field)):
        new_field.append([])
        for j in range(field[i]):
            new_field[i].append(1)
    for i in range(len(piece)):
        for j in range(len(piece[i])):
            new_field[i+x].append(piece[i][j])
    return new_field

def piece_fits_at(piece, field, x, y):
    if not piece_fits(piece, field):
        return False
    for i in range(len(piece)):
        for j in range(len(piece[i])):
            if (piece[i][j] == 1) and (field[i+x] - y >= 100 or field[i+x] - y < 0):
                return False
            if (piece[i][j] == 1) and (field[i+x] - y >= 0) and (field[i+x] - y < len(field[i+x])) and (field[i+x][field[i+x] - y] == 1):
                return False
    return True

def count_places(piece, field):
    count = 0
    for i in range(len(field) - len(piece) + 1):
        for j in range(len(field[i])):
            if piece_fits_at(piece, field, i, j):
                count += 1
    return count

def main():
    _, piece_num = map(int, input().strip().split())
    field = list(map(int, input().strip().split()))
    pieces = [
        [[0, 1, 0], [1, 1, 1]],
        [[0, 1], [1, 1], [0, 1]],
        [[0, 1, 0], [0, 1, 1], [0, 1, 0]],
        [[1, 1, 1, 1]],
        [[1, 1], [1, 1]],
        [[1, 1, 1], [0, 1, 0]],
        [[1, 1, 1], [0, 0, 1]]
    ]
    piece = pieces[piece_num - 1]
    for i in range(3):
        piece = rotated_piece(piece)
        count = count_places(piece, field)
        print(count)

main()
