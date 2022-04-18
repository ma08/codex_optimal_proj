

n = int(input())

# create the board
board = [[0 for i in range(n)] for i in range(n)]

# populate the board
for i in range(n):
    x,y = [int(x) for x in input().split()]
    board[x][y] = "Q"

# check the board
for i in range(n):
    for j in range(n):
        if board[i][j] == "Q":
            # check the row
            for k in range(n):
                if board[i][k] == "Q" and k != j:
                    print("INCORRECT")
                    exit(0)
            # check the column
            for k in range(n):
                if board[k][j] == "Q" and k != i:
                    print("INCORRECT")
                    exit(0)
            # check the diagonals
            # check up and to the left
            x = i
            y = j
            while x > 0 and y > 0:
                x -= 1
                y -= 1
                if board[x][y] == "Q":
                    print("INCORRECT")
                    exit(0)
            # check up and to the right
            x = i
            y = j
            while x > 0 and y < n-1:
                x -= 1
                y += 1
                if board[x][y] == "Q":
                    print("INCORRECT")
                    exit(0)
            # check down and to the left
            x = i
            y = j
            while x < n-1 and y > 0:
                x += 1
                y -= 1
                if board[x][y] == "Q":
                    print("INCORRECT")
                    exit(0)
            # check down and to the right
            x = i
            y = j
            while x < n-1 and y < n-1:
                x += 1
                y += 1
                if board[x][y] == "Q":
                    print("INCORRECT")
                    exit(0)

print("CORRECT")
