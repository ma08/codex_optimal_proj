

# Solution

# Get input
word = input()

# Get number of characters
length = len(word)

# Create a list of the characters
letters = list(word)

# Create a list of the frames
frames = []
for i in range(length):
    if i % 3 == 0:
        frames.append("*")
    else:
        frames.append("#")

# Print the top frame
for i in range(length):
    print("."+frames[i]+".", end="")
print()

# Print the middle frame
for i in range(length):
    print(frames[i]+"."+letters[i]+"."+frames[i], end="")
print()

# Print the bottom frame
for i in range(length):
    print("."+frames[i]+".", end="")
print()
