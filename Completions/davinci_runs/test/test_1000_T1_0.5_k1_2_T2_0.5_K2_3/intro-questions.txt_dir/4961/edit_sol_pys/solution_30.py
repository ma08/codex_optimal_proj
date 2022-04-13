
# Get input from user
input_list = []

while True:
    try:
        input_list.append(input())
    except EOFError:
        break

# Parse input
R, C = input_list[0].split()
R = int(R) # number of rows
C = int(C) # number of columns

# Initialize number of handshakes to zero
num_handshakes = 0 

# Iterate through matrix
for i in range(1, R+1):
    for j in range(0, C):
        if input_list[i][j] == 'o':
            if i < R and input_list[i+1][j] == 'o':
                num_handshakes += 1
            if i > 1 and input_list[i-1][j] == 'o':
                num_handshakes += 1
            if j < C-1 and input_list[i][j+1] == 'o':
                num_handshakes += 1
            if j > 0 and input_list[i][j-1] == 'o':
                num_handshakes += 1
            if i < R and j < C-1 and input_list[i+1][j+1] == 'o':
                num_handshakes += 1
            if i > 1 and j > 0 and input_list[i-1][j-1] == 'o':
                num_handshakes += 1
            if i < R and j > 0 and input_list[i+1][j-1] == 'o':
                num_handshakes += 1
            if i > 1 and j < C-1 and input_list[i-1][j+1] == 'o':
                num_handshakes += 1

# Print result
print(num_handshakes)
