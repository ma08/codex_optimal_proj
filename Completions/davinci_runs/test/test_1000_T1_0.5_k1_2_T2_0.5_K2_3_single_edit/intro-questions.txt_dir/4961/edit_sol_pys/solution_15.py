

# Get input from user
input_list = []

while True:
    try:
        input_list.append(input())
    except:
        break

# Parse input
n_rows, n_cols = input_list[0].split()
n_rows = int(n_rows)
n_cols = int(n_cols)

# Initialize number of handshakes
num_handshakes = 0

# Iterate through matrix
for i in range(1, n_rows+1):
    for j in range(0, n_cols):
        if input_list[i][j] == 'o':
            if i < n_rows and input_list[i+1][j] == 'o':
                num_handshakes += 1
            if i > 1 and input_list[i-1][j] == 'o':
                num_handshakes += 1
            if j < n_cols-1 and input_list[i][j+1] == 'o':
                num_handshakes += 1
            if j > 0 and input_list[i][j-1] == 'o':
                num_handshakes += 1
            if i < n_rows and j < n_cols-1 and input_list[i+1][j+1] == 'o':
                num_handshakes += 1
            if i > 1 and j > 0 and input_list[i-1][j-1] == 'o':
                num_handshakes += 1
            if i < n_rows and j > 0 and input_list[i+1][j-1] == 'o':
                num_handshakes += 1
            if i > 1 and j < n_cols-1 and input_list[i-1][j+1] == 'o':
                num_handshakes += 1

# Print result
print(num_handshakes)
