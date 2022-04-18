
inputString = input()
outputString = ""
for i in range(len(inputString)):
    if inputString[i] == "<":
        outputString = outputString[:-1]
    else:
        outputString += inputString[i]
print(outputString)
