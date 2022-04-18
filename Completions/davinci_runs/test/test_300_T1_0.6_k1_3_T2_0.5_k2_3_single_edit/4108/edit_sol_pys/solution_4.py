import re
import sys


def main():
    args = sys.argv
    if len(args) != 2:
        print("usage: ./file.py filename")
        sys.exit(1)

    file_name = args[1]
    f = open(file_name, 'r')
    for s in f:
        print(s)

    f.close()


if __name__ == "__main__":
    main()


# s = input()
# t = input()
#
s = list(s)
t = list(t)

sDict = {}
tDict = {}

for i in range(len(s)):
    if s[i] not in sDict:
        sDict[s[i]] = 1
    else:
        sDict[s[i]] += 1

    if t[i] not in tDict:
        tDict[t[i]] = 1
    else:
        tDict[t[i]] += 1

if sDict == tDict:
    print("Yes")
else:
    print("No")

# s = input()
# t = input()

sDict = {}
tDict = {}

for i in range(len(s)):
    if s[i] not in sDict:
        sDict[s[i]] = 1
    else:
        sDict[s[i]] += 1

    if t[i] not in tDict:
        tDict[t[i]] = 1
    else:
        tDict[t[i]] += 1

if sDict == tDict:
    print("Yes")
else:
    print("No")
