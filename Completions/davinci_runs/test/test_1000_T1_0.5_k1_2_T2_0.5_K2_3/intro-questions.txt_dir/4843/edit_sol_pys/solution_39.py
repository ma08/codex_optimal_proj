

N = int(input())

# Initialize a 2-D array to store the positions of the queens
positions = [[0 for x in range(N)] for x in range(N)]

# Read in the positions and store them in the 2-D array
for i in range(N):
    x, y = map(int, input().split())
    positions[x][y] = 1

# Initialize a flag to check if there are any queens attacking each other
flag = True


for i in range(N):
    for j in range(N):
        if positions[i][j] == 1:
            for k in range(N):
                if positions[i][k] == 1 and k != j:
                    flag = False
                    break
            for k in range(N):
                if positions[k][j] == 1 and k != i:
                    flag = False
                    break
            for k in range(N):
                if i+k < N and j+k < N and positions[i+k][j+k] == 1 and k != 0:
                    flag = False
                    break
                if i-k > -1 and j-k > -1 and positions[i-k][j-k] == 1 and k != 0:
                    flag = False
                    break
                if i+k < N and j-k > -1 and positions[i+k][j-k] == 1 and k != 0:
                    flag = False
                    break
                if i-k > -1 and j+k < N and positions[i-k][j+k] == 1 and k != 0:
                    flag = False
                    break

if flag:
    print("CORRECT")
else:
    print("INCORRECT")
