


def bingo(a, b):
    """
    Return whether there is a bingo.
    :param a: 2D list
    :param b: 1D list
    :return: bool
    """
    # Make a set for each row and column
    row = [set() for _ in range(3)]
    col = [set() for _ in range(3)]
    # Make a set for the two diagonals
    diag = [set(), set()]
    # Iterate through the bingo card and mark the numbers that are in b
    for i in range(3):
        for j in range(3):
            if a[i][j] in b:
                row[i].add(a[i][j])
                col[j].add(a[i][j])
                if i == j:
                    diag[0].add(a[i][j])
                if i + j == 2:
                    diag[1].add(a[i][j])
    # Check whether there is a bingo
    bingo = False
    for i in range(3):
        if len(row[i]) == 3 or len(col[i]) == 3:
            bingo = True
            break
    if not bingo:
        for diag_set in diag:
            if len(diag_set) == 3:
                bingo = True
                break
    return bingo


def main():
    # Read input from stdin
    a = []
    for _ in range(3):
        a.append(list(map(int, input().split())))
    n = int(input())
    b = []
    for _ in range(n):
        b.append(int(input()))
    # Print output
    if bingo(a, b):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()