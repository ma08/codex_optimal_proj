

n = int(input())
prefixes = []
suffixes = []

for i in range(2 * n - 2):
    prefixes.append(input())

for i in range(2 * n - 2):
    suffixes.append(input())

for i in range(2 * n - 2):
    if i < n - 1:
        print("P", end="")
    else:
        print("S", end="")
