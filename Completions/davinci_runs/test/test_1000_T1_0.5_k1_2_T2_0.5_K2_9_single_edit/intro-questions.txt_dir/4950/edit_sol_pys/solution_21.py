

def main():
    """
    input:
        n: number of test cases
        m: size of grid
        k: number of obstacles
        r_q: row of queen
        c_q: column of queen
        obstacle: row, column of obstacle
    output:
        number of squares in all directions
    """
    n = int(input())
    for _ in range(n):
        m, k = map(int, input().split())
        r_q, c_q = map(int, input().split())
        obstacles = []
        for _ in range(k):
            r, c = map(int, input().split())
            obstacles.append((r, c))
        print(calculate_squares(m, k, r_q, c_q, obstacles))

def calculate_squares(m, k, r_q, c_q, obstacles):
    """
    input:
        m: size of grid
        k: number of obstacles
        r_q: row of queen
        c_q: column of queen
        obstacle: row, column of obstacle
    output:
        number of squares in all directions
    """
    squares = 0
    for r in range(1, m + 1):
        for c in range(1, m + 1):
            if (r, c) in obstacles:
                continue
            if valid_square(m, r_q, c_q, r, c):
                squares += 1
    return squares

def valid_square(m, r_q, c_q, r, c):
    """
    input:
        m: size of grid
        r_q: row of queen
        c_q: column of queen
        r: row of square
        c: column of square
    output:
        True if square is valid
        False if square is invalid
    """
    if r == r_q or c == c_q:
        return True
    if abs(r - r_q) == abs(c - c_q):
        return True
    return False

def calculate_squares_old(m, k, r_q, c_q, obstacles):
    """
    input:
        m: size of grid
        k: number of obstacles
        r_q: row of queen
        c_q: column of queen
        obstacle: row, column of obstacle
    output:
        number of squares in all directions
    """
    squares = 0
    squares += calculate_squares_vertical(m, k, r_q, c_q, obstacles)
    squares += calculate_squares_horizontal(m, k, r_q, c_q, obstacles)
    squares += calculate_squares_diagonal(m, k, r_q, c_q, obstacles)
    return squares

def calculate_squares_vertical(m, k, r_q, c_q, obstacles):
    """
    input:
        m: size of grid
        k: number of obstacles
        r_q: row of queen
        c_q: column of queen
        obstacle: row, column of obstacle
    output:
        number of squares in vertical direction
    """
    squares = 0
    for r in range(1, m + 1):
        if (r, c_q) in obstacles:
            continue
        squares += 1
    return squares

def calculate_squares_horizontal(m, k, r_q, c_q, obstacles):
    """
    input:
        m: size of grid
        k: number of obstacles
        r_q: row of queen
        c_q: column of queen
        obstacle: row, column of obstacle
    output:
        number of squares in horizontal direction
    """
    squares = 0
    for c in range(1, m + 1):
        if (r_q, c) in obstacles:
            continue
        squares += 1
    return squares

def calculate_squares_diagonal(m, k, r_q, c_q, obstacles):
    """
    input:
        m: size of grid
        k: number of obstacles
        r_q: row of queen
        c_q: column of queen
        obstacle: row, column of obstacle
    output:
        number of squares in diagonal direction
    """
    squares = 0
    for r in range(1, m + 1):
        for c in range(1, m + 1):
            if (r, c) in obstacles:
                continue
            if abs(r - r_q) == abs(c - c_q):
                squares += 1
    return squares

def calculate_squares_diagonal_old(m, k, r_q, c_q, obstacles):
    """
    input:
        m: size of grid
        k: number of obstacles
        r_q: row of queen
        c_q: column of queen
        obstacle: row, column of obstacle
    output:
        number of squares in diagonal direction
    """
    squares = 0
    for r in range(r_q, 1, -1):
        if (r, c_q - (r_q - r)) in obstacles:
            break
        squares += 1
    for r in range(r_q, m + 1):
        if (r, c_q + (r - r_q)) in obstacles:
            break
        squares += 1
    for c in range(c_q, 1, -1):
        if (r_q - (c_q - c), c) in obstacles:
            break
        squares += 1
    for c in range(c_q, m + 1):
        if (r_q + (c - c_q), c) in obstacles:
            break
        squares += 1
    return squares

def calculate_squares_old(m, k, r_q, c_q, obstacles):
    """
    input:
        m: size of grid
        k: number of obstacles
        r_q: row of queen
        c_q: column of queen
        obstacle: row, column of obstacle
    output:
        number of squares in all directions
    """
    squares = 0
    for _ in range(n):
        r, c = map(int, input().split())
        if r == r_q or c == c_q or abs(r - r_q) == abs(c - c_q):
            squares += 1
    return squares

if __name__ == "__main__":
    main()
