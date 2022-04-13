
#get the number of words
import sys

#initialize an empty list
N = int(input())
words = []
#get the words
s = set()
for i in range(N):
    s.add(input())
#check if the words are connected
words = list(s)
for i in range(N):
    if i == 0:
        pass
    else:
        if words[i][0] != words[i-1][-1]:
            print('No')
            sys.exit()

print('Yes')
