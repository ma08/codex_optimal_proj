

inputString = input("Enter your string: ")
outputString = ""

for i in range(len(inputString)):
    if inputString[i] == "<":
        outputString = outputString[:-1]
    else:
        outputString += inputString[i]

print("Output string: " + outputString)
