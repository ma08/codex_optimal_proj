def getMinMoves(n, s):
    if n <= s:
        return n
    else:    
        moves = n
        for i in range(n):
            if i > s:
                break
            moves = min(moves, getMinMoves(n - i, s) + 1)
        return moves
