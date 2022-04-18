

# Solution 1

word = input() # Get input

length = len(word) # Get number of characters

letters = list(word) # Create a list of the characters

frames = [] # Create a list of the frames
for i in range(length):
    if i%3 == 0:
        frames.append("*")
    else:
        frames.append("#")

for i in range(length):
    print("."+frames[i]+".", end="") # Print the top frame
print() # New line

for i in range(length):
    print(frames[i]+"."+letters[i]+"."+frames[i], end="") # Print the middle frame
print() # New line

for i in range(length):
    print("."+frames[i]+".", end="") # Print the bottom frame
print() # New line
