

def bingo(A, b):
    """
    >>> bingo([[84, 97, 66], [79, 89, 11], [61, 59, 7]], [89, 7, 87, 79, 24, 84, 30])
    'Yes'
    >>> bingo([[82, 89, 83], [79, 83, 39], [87, 34, 83]], [55, 31, 77, 82, 85, 61, 74, 55, 89, 85])
    'No'
    """
    for i in range(3):
        for j in range(3):
            if A[i][j] in b:
                A[i][j] = 1
    if sum(A[0]) == 3 or sum(A[1]) == 3 or sum(A[2]) == 3:
        return 'Yes'
    elif sum([A[i][0] for i in range(3)]) == 3 or sum([A[i][1] for i in range(3)]) == 3 or sum([A[i][2] for i in range(3)]) == 3:
        return 'Yes'
    elif sum([A[i][i] for i in range(3)]) == 3 or sum([A[i][2-i] for i in range(3)]) == 3:
        return 'Yes'
    else:
        return 'No'

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    A = []
    for i in range(3):
        A.append(list(map(int, input().split())))
    N = int(input())
    b = []
    for i in range(N):
        b.append(int(input()))
    print(bingo(A, b))