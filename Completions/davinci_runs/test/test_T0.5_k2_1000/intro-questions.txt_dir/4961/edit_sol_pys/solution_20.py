

# Get input from user
input_list = []
while True:
    try:
        input_list.append(input())
    except:
        break

# Parse input
R, S = input_list[0].split()
R = int(R)
S = int(S)

# Initialize number of people
num_people = 0

# Iterate through matrix
for i in range(1, R+1):
    for j in range(0, S):
        if input_list[i][j] == 'o':
            num_people += 1
            if i < R and input_list[i+1][j] == 'o':
                num_people += 1
            if i > 1 and input_list[i-1][j] == 'o':
                num_people += 1
            if j < S-1 and input_list[i][j+1] == 'o':
                num_people += 1
            if j > 0 and input_list[i][j-1] == 'o':
                num_people += 1
            if i < R and j < S-1 and input_list[i+1][j+1] == 'o':
                num_people += 1
            if i > 1 and j > 0 and input_list[i-1][j-1] == 'o':
                num_people += 1
            if i < R and j > 0 and input_list[i+1][j-1] == 'o':
                num_people += 1
            if i > 1 and j < S-1 and input_list[i-1][j+1] == 'o':
                num_people += 1

# Calculate number of handshakes
num_handshakes = num_people * (num_people - 1) // 2

# Print result
print(num_handshakes)
