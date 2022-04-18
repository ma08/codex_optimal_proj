

inputString = input()
outputString = ""

for i in range(0, len(inputString)):
    if inputString[i] == "<":
        outputString = outputString[:-1]
    else:
        outputString += inputString[i]

print(outputString)
