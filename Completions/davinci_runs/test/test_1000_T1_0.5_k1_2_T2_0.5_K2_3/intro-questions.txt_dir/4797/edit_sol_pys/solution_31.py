inputString = input()
outputString = ""

for i in inputString:
    if i == "<":
        outputString = outputString[:-1]
    else:
        outputString += i

print(outputString)
