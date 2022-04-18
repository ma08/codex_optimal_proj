#Solution #1

#Get input
word = input()

#Get number of characters
length = len(word)

#Create a list of the characters
letters = list(word)

#Create a list of the frames
frames = []
for i in range(length):
    if i%3 == 0:
        frames.append("*")
    else:
        frames.append("#")

#Print the top frame
for i in range(length):
    print(".%s." % (frames[i]), end="")
print()

#Print the middle frame
for i in range(length):
    print("%s.%s.%s" % (frames[i], letters[i], frames[i]), end="")
print()

#Print the bottom frame
for i in range(length):
    print(".%s." % (frames[i]), end="")
print()
