
import sys
input = sys.stdin.readline

n = int(input())
words = []
for i in range(n):
    words.append(input().strip())

if len(words) == len(set(words)):
    if n == 1:
        print("Fair Game")
    elif words[0][-1] == words[1][0]:
        for i in range(1, n-1):
            if words[i][-1] != words[i+1][0]:
                print("Player {} lost".format(i%2 + 1))
                break
        else:
            print("Fair Game.")
    else:
        print("Player 1 lost")
else:
    for i in range(n-1):
        if words[i] == words[i+1]:
            print("Player {} lost".format(i%2 + 1))
            break
