

inputString = input()
outputString = ""

for i in range(len(inputString)): # loop through the input string
    if inputString[i] == "<": # if the current character is '<'
        outputString = outputString[:-1]
    else:
        outputString += inputString[i]

print(outputString)
