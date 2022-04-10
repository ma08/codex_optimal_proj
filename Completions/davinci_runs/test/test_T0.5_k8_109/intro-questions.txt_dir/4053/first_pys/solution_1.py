

# SOLUTION
n = int(input())
prefixes = []
suffixes = []
for i in range(2*n-2):
    string = input()
    if string[0] == "a":
        prefixes.append(string)
    else:
        suffixes.append(string)

for i in range(len(prefixes)):
    print("P", end="")
for i in range(len(suffixes)):
    print("S", end="")