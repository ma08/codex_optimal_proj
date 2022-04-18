

# Read the inputs
n = int(input())
s = input().strip()

# Check if the input is valid
if n < 1 or n > 100000:
    print("Invalid input")
    exit(1)

# Check if the string is valid
if len(s) != n:
    print("Invalid input")
    exit(1)

# Check if the string has only 0's and 1's
if s.count("0") + s.count("1") != n:
    print("Invalid input")
    exit(1)

# Initialize variables
max_cnt = 0
cnt = 0

# Loop through the string
for i in range(n):
    # If a 1 is encountered, increment the counter
    if s[i] == "1":
        cnt += 1
        # Update the max_cnt if required
        if cnt > max_cnt:
            max_cnt = cnt
    # If a 0 is encountered, reset the counter
    else:
        cnt = 0

# Print the result
if max_cnt % 2 == 0:
    print("Even")
else:
    print("Odd")
