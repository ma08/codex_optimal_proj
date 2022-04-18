

from sys import stdin

word = stdin.readline().strip()
endings = []
for i in range(int(stdin.readline().strip())):
    endings.append(stdin.readline().strip().split())
for i in range(int(stdin.readline().strip())):
    phrase = stdin.readline().strip().split()
    if len(phrase) == 2:
        if word.endswith(phrase[1]):
            print("YES")
        else:
            print("NO")
    else:
        if word.endswith(phrase[1]) or word.endswith(phrase[2]):
            print("YES")
        else:
            print("NO")
