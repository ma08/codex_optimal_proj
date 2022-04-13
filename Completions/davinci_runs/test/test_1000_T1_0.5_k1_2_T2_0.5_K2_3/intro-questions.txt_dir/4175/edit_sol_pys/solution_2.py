
#get the number of words
import sys

#initialize an empty list
N = int(input())
words = []
#get the words

for i in range(N):
    words.append(input())
#check if the words are connected

for i in range(N):
    if i == 0:
        pass
    else:
        if words[i] in words[:i]:
            print('No')
            sys.exit()
        if words[i][0] != words[i-1][-1]:
            print('No')
            sys.exit()

print('Yes')
