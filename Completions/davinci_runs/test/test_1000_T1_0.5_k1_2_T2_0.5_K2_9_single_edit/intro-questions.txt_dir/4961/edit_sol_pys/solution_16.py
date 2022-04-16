

# Get input from user
input_list = ["3 3", "o.o", ".o.", "o.o"]

# while True:
#     try:
#         input_list.append(input())
#     except:
#         break

# Parse input
R, S = input_list[0].split()
R = int(R)
S = int(S)

# Initialize number of handshakes
num_handshakes = 0

# Iterate through matrix
for i in range(0, R):
    for j in range(0, S-1):
        if input_list[i][j] == 'o':
            if i < R and input_list[i+1][j] == 'o':
                num_handshakes += 1
            if i > 0 and input_list[i-1][j] == 'o':
                num_handshakes += 1
            if j < S-1 and input_list[i][j+1] == 'o':
                num_handshakes += 1
            if j > 0 and input_list[i][j-1] == 'o':
                num_handshakes += 1
            if i < R and j < S-1 and input_list[i+1][j+1] == 'o':
                num_handshakes += 1
            if i > 0 and j > 0 and input_list[i-1][j-1] == 'o':
                num_handshakes += 1
            if i < R and j > 0 and input_list[i+1][j-1] == 'o':
                num_handshakes += 1
            if i > 0 and j < S-1 and input_list[i-1][j+1] == 'o':
                num_handshakes += 1

# Print result
print(num_handshakes)
