

def min_moves(pieces, target_coordinates):
    moves_required = 0
    target_coordinates.sort()


    for i in range(len(pieces)):
        moves_required += abs(pieces[i] - target_coordinates[i])

    return moves_required // 2


if __name__ == '__main__':
    n, m = map(int, input().split())
    x = list(map(int, input().split()))

    print(min_moves(x, list(range(1, n + 1))))
